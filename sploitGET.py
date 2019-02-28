import argparse
import json
import re
import subprocess
import sys

import colorama as clr
import prettytable
import pyfiglet
import requests


class Sploitus:

    @staticmethod
    def __version__():
        return 0.1

    def __init__(self, query, qtype, sort):
        self._banner()
        self.query = query
        self.type = qtype
        self.sort = sort
        self.url = 'https://sploitus.com/search'
        self.header = {'content-type': 'application/json'}

    def _init_search_dict(self):
        qdict = dict()
        qdict['type'] = self.type
        qdict['sort'] = self.sort
        qdict['query'] = self.query
        qdict['title'] = False
        qdict['offset'] = 0
        return qdict

    def _banner(self):
        custom_fig = pyfiglet.Figlet(font='banner')
        print(custom_fig.renderText('SploitGET'))

    def exec_query(self):
        query_dict = self._init_search_dict()
        response = json.loads(requests.post(self.url, headers=self.header, data=json.dumps(query_dict)).text)
        if int(response['exploits_total']):
            print(clr.Fore.GREEN + '[+] Found {} results!\n'.format(response['exploits_total']) + clr.Fore.RESET)
            if self.type == 'exploits':
                self._parse_exploit_query_results(response)
            elif self.type == 'tools':
                self._parse_tools_query_results(response)
        else:
            print(clr.Fore.RED + '[!] No Results found\n' + clr.Fore.RESET)
            sys.exit(1)

    @staticmethod
    def _parse_exploit_query_results(response):
        rem_chin = re.compile(u'[⺀-⺙⺛-⻳⼀-⿕々〇〡-〩〸-〺〻㐀-䶵一-鿃豈-鶴侮-頻並-龎]', re.UNICODE)
        res = prettytable.PrettyTable()
        res.max_width = int(subprocess.check_output(['stty', 'size'], encoding='utf-8').split()[1])
        res.field_names = ['Title', 'URL', 'Date', 'Published', 'Score']
        for entry in response['exploits']:
            if len(entry['title'].replace('&quot;', '')) > 45:
                res.add_row([rem_chin.sub('', entry['title'].replace('&quot;', '')[:45]), entry['href'], entry['published'], entry['type'], entry['score']])
            else:
                res.add_row([rem_chin.sub('', entry['title'].replace('&quot;', '')), entry['href'], entry['published'], entry['type'], entry['score']])
        print(res)

    @staticmethod
    def _parse_tools_query_results(response):
        res = prettytable.PrettyTable()
        res.max_width = int(subprocess.check_output(['stty', 'size'], encoding='utf-8').split()[1])
        res.field_names = ['Title', 'URL', 'Blog']
        for entry in response['exploits']:
            if len(entry['title'].replace('&quot;', '')) > 45:
                res.add_row([entry['title'].replace('&quot;', '')[:45], entry['download'], entry['href']])
            else:
                res.add_row([entry['title'].replace('&quot;', ''), entry['download'], entry['href']])
        print(res)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--query', type=str, help='search query', required=True)
    parser.add_argument('-t', '--type', type=str, default='exploits', choices=['exploits', 'tools'],
                        help='Search for either public exploits or tools')
    parser.add_argument('-s', '--sort', type=str, default='default', choices=['default', 'date', 'score'],
                        help='Sort the results by chosen option')
    args = parser.parse_args()
    sploit = Sploitus(query=args.query, qtype=args.type, sort=args.sort)
    sploit.exec_query()


if __name__ == '__main__':
    sys.exit(main())
