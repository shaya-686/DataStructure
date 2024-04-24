import pickle
import gzip


class Countries:
    country_file_pickle = 'country.pickle'

    def __init__(self):
        self.countries = {
            "United States": "Washington, D.C.",
            "United Kingdom": "London",
            "France": "Paris",
            "Germany": "Berlin",
            "China": "Beijing",
            "Brazil": "Brasília",
            "Japan": "Tokyo",
            "India": "New Delhi",
            "Australia": "Canberra",
            "Ukraine": "Kyiv"
        }

    def add_country(self, country, capital):
        if country in self.countries:
            raise ValueError("The country already exists")
        self.countries[country] = capital
        self.upload_countries()

    def remove_country(self, country):
        if not self.countries:
            raise IndexError("Dictionary is empty")
        if country not in self.countries:
            raise ValueError("Country not found")
        del self.countries[country]
        self.upload_countries()

    def change_country(self, country, capital):
        if not self.countries:
            raise IndexError("Dictionary is empty")
        if country not in self.countries:
            raise ValueError("Country not found")
        self.countries[country] = capital
        self.upload_countries()

    def find_country(self, country):
        if not self.countries:
            raise IndexError("Dictionary is empty")
        if country in self.countries:
            print(f"Country found: country - {country}, capital - {self.countries[country]}")

    def upload_countries(self):
        if not self.countries:
            raise IndexError("Dictionary is empty")
        with open(self.country_file_pickle, 'wb') as pickle_file:
            pickle.dump(self.countries, pickle_file)

    def download_countries(self):
        with open(self.country_file_pickle, 'rb') as pickle_file:
            read_countries = pickle.load(pickle_file)
        print(f"Origin list = {self.countries} \nPickle list = {read_countries}")

    def print_countries(self):
        if not self.countries:
            raise IndexError("Dictionary is empty")
        for key, value in self.countries.items():
            print(f"Country: {key}, capital: {value}")


countries = Countries()

try:

    countries.print_countries()

    countries.upload_countries()
    countries.download_countries()

    countries.find_country("Ukraine")

    countries.add_country("Italy", "Roma")
    countries.download_countries()

    countries.remove_country("Germany")
    countries.download_countries()

    countries.change_country("India", "New-Delhi")
    countries.download_countries()

    countries.add_country("India", "Roma")
    countries.download_countries()

except ValueError as e:
    print("Message: ", e)
except IndexError as e:
    print("Message: ", e)
except Exception as e:
    print("Message: ", e)


class Bands:
    bands_file_gzip = 'bands.gzip'

    def __init__(self):
        self.bands = {
            "Depeche Mode": {"Memento mori", "Spirit", "Delta Machine", "Sounds of the Universe", "Playing the Angel",
                             "Exciter", "Ultra", "Songs of Faith and Devotion", "Violator", "Music for the Masses",
                             "Black Celebration", "Some Great Reward", "Construction Time Again", "A Broken Frame",
                             "Speak & Spell"},
            "Queen": {"Queen", "Queen II", "Sheer Heart Attack", "A Night at the Opera", "A Day at the Races",
                      "News of the World", "Jazz", "The Game", "Flash Gordon", "Hot Space", "The Works",
                      "A Kind of Magic", "The Miracle", "Innuendo", "Made in Heaven"},
            "Imagine Dragons": {"Night Visions", "Smoke + Mirrors", "Evolve", "Origins"},
            "Океан Ельзи": {"Там, де нас нема", "Янанебібув", "Суперсиметрія", "GLORIA", "Dolce Vita", "Модель",
                            "Земля", "Без меж", "Міра"}}

    def add_band(self, band, album):
        if band in self.bands:
            raise ValueError("The band already exists")
        self.bands[band] = {album}
        self.upload_bands()

    def remove_band(self, band):
        if not self.bands:
            raise IndexError("Dictionary is empty")
        if band not in self.bands:
            raise ValueError("Band not found")
        del self.bands[band]
        self.upload_bands()

    def add_album(self, band, album):
        if not self.bands:
            raise IndexError("Dictionary is empty")
        if band not in self.bands:
            raise ValueError("Band not found")
        self.bands[band].add(album)
        self.upload_bands()

    def remove_album(self, band, album):
        if not self.bands:
            raise IndexError("Dictionary is empty")
        if band not in self.bands:
            raise ValueError("Band not found")
        self.bands[band].remove(album)
        self.upload_bands()

    def change_band(self, band, album, new_album):
        if not self.bands:
            raise IndexError("Dictionary is empty")
        if band not in self.bands:
            raise ValueError("Band not found")
        self.bands[band].remove(album)
        self.bands[band].add(new_album)
        self.upload_bands()

    def find_band(self, band):
        if not self.bands:
            raise IndexError("Dictionary is empty")
        if band in self.bands:
            print(f"Band found: band - {band}, albums - {self.bands[band]}")

    def upload_bands(self):
        if not self.bands:
            raise IndexError("Dictionary is empty")
        with gzip.open(self.bands_file_gzip, 'wb') as gzip_file:
            serialized = pickle.dumps(self.bands)
            gzip_file.write(serialized)

    def download_bands(self):
        with gzip.open(self.bands_file_gzip, 'rb') as gzip_file:
            serialized = gzip_file.read()
            read_bands = pickle.loads(serialized)
        print(f"Origin list = {self.bands} \nGzip list = {read_bands}")

    def print_bands(self):
        if not self.bands:
            raise IndexError("Dictionary is empty")
        for key, value in self.bands.items():
            print(f"Band: {key}, albums: {value}")


bands = Bands()
try:

    bands.upload_bands()
    bands.download_bands()

    bands.add_band("Maneskin", "Rush!")
    bands.download_bands()

    bands.change_band("Maneskin", "Rush!", "Rush1!")
    bands.download_bands()

    bands.remove_band("Maneskin")
    bands.download_bands()

    bands.find_band("Depeche Mode")

    bands.add_album("Depeche Mode", "New")
    bands.download_bands()

    bands.remove_album("Depeche Mode", "New")
    bands.download_bands()

    bands.print_bands()
except ValueError as e:
    print("Message: ", e)
except IndexError as e:
    print("Message: ", e)
except Exception as e:
    print("Message: ", e)
