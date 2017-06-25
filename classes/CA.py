import requests, time, random, string, os
from faker import Faker
from bs4 import BeautifulSoup
fake = Faker()
def account_successfully_createdCA(response):
        try:
            return False if BeautifulSoup(response.text, "html.parser").find('input',
                                                                             {'id': 'resumeURL'}).get('value') == \
                            'https://www.adidas.ca/on/demandware.store/Sites-adidas-CA-Site/en_CA/MyAccount-CreateOrLogin' \
                else True
        except:
            return True

def CA(x, domain):

    for i in range(x):
        first = fake.first_name()
        last = fake.last_name()
        number = random.randint(0, 999)
        email = '{}{}{}@{}'.format(first, number, last, domain)
        password = '{}{}{}'.format(first, number, last)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, sdch, br',
            'Accept-Language': 'en-US,en;q=0.8',
            'Upgrade-Insecure-Requests': '1'
        }
        s = requests.Session()
        s.headers.update(headers)
        r = s.get('https://cp.adidas.ca/web/eCom/en_CA/loadcreateaccount')
        csrftoken = BeautifulSoup(r.text, "html.parser").find('input', {'name': 'CSRFToken'}).get('value')

        s.headers.update({
            'Origin': 'https://cp.adidas.ca',
            'Referer': 'https://cp.adidas.ca/web/eCom/en_CA/loadcreateaccount',
        })
        r = s.post('https://cp.adidas.ca/web/eCom/en_CA/accountcreate',
                   data={
                       'firstName': first,
                       'lastName': last,
                       'minAgeCheck': 'true',
                       '_minAgeCheck': 'on',
                       'email': email,
                       'password': password,
                       'confirmPassword': password,
                       'amf': 'true',
                       '_amf': 'on',
                       'terms': 'true',
                       '_terms': 'on',
                       'metaAttrs[pageLoadedEarlier]': 'true',
                       'app': 'eCom',
                       'locale': 'en_CA',
                       'domain': '',
                       'consentData1': 'Sign me up for adidas emails, featuring exclusive offers, featuring latest product info, news about upcoming events, and more. See our <a target="_blank" href="https://www.adidas.com/us/help-topics-privacy_policy.html">Policy Policy</a> for details.',
                       'consentData2': 'By entering my information, I give permission for adidas Canada Limited to contact me in future for marketing, advertising and opinion research for purposes of the adidas Group. I understand I can later withdraw consent.<a target="_blank" href="http://www.adidas.ca/en/help-topics-privacy_policy.html"><b>Learn More</b></a',
                       'consentData3': '',
                       'CSRFToken': csrftoken
                   })
        print("Created Account : Username = {0}, Password = {1}".format(email, password))
        with open('accountsCA.txt', 'a') as f:
            f.write(email + ':' + password + '\n')
            f.close()

        time.sleep(2)
