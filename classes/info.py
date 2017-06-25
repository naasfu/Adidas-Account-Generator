from classes.US import USGEN
from classes.UK import UKGEN
from classes.AU import AUGEN
from classes.CA import CA

USGEN = USGEN()
UKGEN = UKGEN()
AUGEN = AUGEN()


class Info:
	def start(self):
		#washed code
		print("Account Generator Ready")

		location = input('Enter Location US UK CA AU: ')
		x = int(input('Number of accounts to be made: '))
		domain = input('Enter in your domain: ')

		if location == 'US':
			USGEN.US(x, domain)

		if location == 'UK':
			UKGEN.UK(x, domain)

		if location == 'AU':
			AUGEN.AU(x, domain)

		if location == 'CA':
			CA(x, domain)
