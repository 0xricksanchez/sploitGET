#! /usr/bin/env python3

import argparse
import json
import re
import subprocess
import sys
import textwrap

import colorama as clr
import prettytable
import pyfiglet
import requests
from pyshorteners import Shortener
from urllib.parse import urlsplit, urlunsplit


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
            res_table = prettytable.PrettyTable()
            res_table.max_width = int(subprocess.check_output(['stty', 'size'], encoding='utf-8').split()[1])
            if self.type == 'exploits':
                self._parse_exploit_query_results(response, res_table)
            elif self.type == 'tools':
                self._parse_tools_query_results(response, res_table)
        else:
            print(clr.Fore.RED + '[!] No Results found\n' + clr.Fore.RESET)

    def _parse_exploit_query_results(self, response, res_table):
        rem_chin = re.compile(u'[⺀-⺙⺛-⻳⼀-⿕々〇〡-〩〸-〺〻㐀-䶵一-鿃豈-鶴侮-頻並-龎]', re.UNICODE)
        res_table.field_names = ['Title', 'URL', 'Date', 'Published', 'Score']
        for entry in response['exploits']:
            title = rem_chin.sub('', entry['title'].replace('&quot;', ''))
            if len(title) > 30:
                res_table.add_row([textwrap.fill(title, 30), self._get_tinyurl(entry['href']),
                                   entry['published'], entry['type'], entry['score']])
            else:
                res_table.add_row([title, self._get_tinyurl(entry['href']), entry['published'],
                                   entry['type'], entry['score']])
            # time.sleep(1) # Depending on the URL shortener there might be a sleep necessary :)
        print(res_table)

    def _parse_tools_query_results(self, response, res_table):
        res_table.field_names = ['Title', 'URL', 'Website']
        for entry in response['exploits']:
            title = entry['title'].replace('&quot;', '')
            if len(title) > 50:
                res_table.add_row([textwrap.fill(title, 50), self._get_tinyurl(entry['download']),
                                   urlsplit(entry['download']).netloc])
            else:
                res_table.add_row([title, self._get_tinyurl(entry['download']), urlsplit(entry['download']).netloc])
        print(res_table)

    @staticmethod
    def _get_tinyurl(url):
        shortener = Shortener('Isgd')
        return shortener.short(url)


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
