from fastai.text.all import *
from fastai.vision.all import *

path = Path("./netflix_data")
best_movie_by_year_df = pd.read_csv(path / "Best Movie By Year Netflix.csv")
best_movies_df = pd.read_csv(path / "Best Movies Netflix.csv")
best_shows_by_year_df = pd.read_csv(path / "Best Shows Netflix.csv")
best_shows_df = pd.read_csv(path / "Best Shows Netflix.csv")
raw_credits_df = pd.read_csv(path / "raw_credits.csv")
raw_titles_df = pd.read_csv(path / "raw_titles.csv")
