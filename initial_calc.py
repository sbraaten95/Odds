"""
>>>>>>> ODDS <<<<<<<<
---------------------
Summary:

Software that calculates the odds for things occurring in every day life.
---------------------

((( Chances of Hooking Up )))

Sources:
	https://www.zavamed.com/uk/one-night-only.html

Statistics:
	Non-gender specific
		How many sexual partners?
			None: 3%
			1-2: 18%
			3-5: 27%
			6-10: 21%
			11-15: 13%
			16-20: 5%
			21-30: 5%
			31+: 7%
			Not sure: 1%

		Ever had one night stand?
			Yes: 66%
			No: 34%

		Planned or spontaneous?
			Planned: 14%
			Spontaneous: 86%

	Gender Specific

		Best places to facilitate one night stands
			Club
				Women: 47%
				Men: 41%
			Bar
				Women: 42%
				Men: 42%
			Mobile app
				Women: 21%
				Men: 26%
			College/University
				Women: 7%
				Men: 12%
			Work
				Women: 5%
				Men: 0%

		Average number of one night stands
			Women: 6
			Men: 7

		Likely to be completely satisfied
			Women: 19%
			Men: 32%

		Who do people tell?
			No one
				Women: 42%
				Men: 34%
			One or two friends
				Women: 54%
				Men: 58%
			Family member
				Women: 2%
				Men: 1%
			All friends
				Women: 2%
				Men: 6%
			Anyone
				Women: 0%
				Men: 1%

	Global
		Number of days between 20 and 39
			6940 days
		DMV Population
			Total: 6,133,552
			20-29: 858,697
			30-39: 920,033
			Age range: 1,778,730
		Median age: 29.5

Factors of Impact:
	Location
	Time
	Group
	Personality
	Past experience
	Goal

Things to calculate:
	Percentage probability change from standard deviation position and trend
	Percentage probability change from venue to venue
	Difference in percentage probability change from different factors of impact
	Trajectories based on standard deviation
	Regression curves
	Closeness of experiences

"""

global_statistics = {
	'first_median_sp': 8,
	'first_sp_per_year': 0.42,
	'first_sp_per_day': 0.0012,
	'first_number_sp_per_age': {
		20: 0,
		21: 0.42,
		22: 0.84,
		23: 1.26,
		24: 1.68,
		25: 2.1,
		26: 2.52,
		27: 2.94,
		28: 3.36,
		29: 3.78,
		30: 4.2,
		31: 4.62,
		32: 5.04,
		33: 5.46,
		34: 5.88,
		35: 6.3,
		36: 6.72,
		37: 7.14,
		38: 7.56,
		39: 7.98,
	}
}

def calc_linear_regression(yrange):
	xsum = 0
	ysum = 0
	xsqsum = 0
	xysum = 0

	keys = global_statistics['first_number_sp_per_age'].keys()

	for i in range(0, len(yrange)):
		xsum += keys[i]
		ysum += yrange[i]
		xsqsum += keys[i] ** 2
		xysum += keys[i] * yrange[i]

	a = ((ysum) * (xsqsum) - (xsum) * (xysum)) / (len(yrange) * xsqsum - xsum ** 2)
	b = float((len(yrange) * xysum - xsum * ysum)) / float((len(yrange) * xsqsum - xsum ** 2))

	return a, b

class User:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.sp_per_year = global_statistics['first_sp_per_year']
		self.sp_per_day = global_statistics['first_sp_per_day']
		self.number_sp_per_age = global_statistics['first_number_sp_per_age']

	def set_sps(self, number):
		self.sps = number
		return self

	def add_sp(self):
		self.sps += 1
		return self

	def calc_stats(self, tpy):
		numrange = []
		for i in range(0, 20 - self.age + 1):
			self.number_sp_per_age[i] = tpy[i]
			numrange.append(tpy[i])
		a, b = calc_linear_regression([3, 0, 0, 5])
		sp_per_year = b
		sp_per_day = b / 365
		return self

class Query:
	def __init__(self, user, event):
		self.user = user
		self.event = event

	def calc_prob(self):
		return self

class Event:
	def __init__(self, ev_id, ev_type):
		self.ev_id = ev_id
		self.ev_type = ev_type

	def set_venue(self, venue):
		self.venue = venue
		return self

class Venue:

	def __init__(self, ven_id, name, street, zipcode):
		self.ven_id = ven_id
		self.name = name
		self.zipcode = zipcode
		self.street = street

	def set_neighborhood(self, neighborhood):
		self.neighborhood = neighborhood

class Neighborhood:
	def __init__(self, n_id, name, state, city):
		self.n_id = n_id
		self.name = name
		self.state = state
		self.city = city

	def add_venue(self, venue):
		if not hasattr(self, 'venues'):
			self.venues = []
		self.venues.append(venue)
		venue.set_neighborhood(self.n_id)
		return self

	def build_venue(self, dataset):
		self.venues = dataset
		return self

scott = User("Scott", 23)
scott.set_sps(5)
scott.calc_stats([3, 0, 0, 5])
