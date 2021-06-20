from lichess_client import APIClient
import pandas as pd

token: str = "... YOUR API TOKEN HERE ..."  # DON'T FORGET TO DELETE BEFORE COMMITTING
output_path: str = "puzzle_history.csv"

# retrieve data
client = APIClient(token=token)
response = await client.users.get_your_puzzle_activity()

# convert to data frame
puzze_history_dict: dict = response.to_dict()
puzzle_history_list: list = puzze_history_dict['entity']['content']
id_buffer: list = list()
date_buffer: list = list()
win_buffer: list = list()
rating_buffer: list = list()

for index in range(len(puzzle_history_list)):
    id_buffer.append(puzzle_history_list[index]['id'])
    date_buffer.append(puzzle_history_list[index]['date'])
    win_buffer.append(puzzle_history_list[index]['win'])
    rating_buffer.append(puzzle_history_list[index]['puzzleRating'])

df = pd.DataFrame()
df['id'] = id_buffer
df['date'] = date_buffer
df['win'] = win_buffer
df['rating'] = rating_buffer

df.to_csv(output_path, index_label='reverse_order')
