import csv
import json
import pickle

def parse_txt(fname):
  """
  Parsing txt files in folder "cornell_movie_dialogs_corpus".
  """
  lines = []
  with open(fname, 'r', encoding='utf-8', errors='replace') as fin:
    for line in fin:
      try:
        lines += [each.strip() for each in line.strip().split('+++$+++')],
      except:
        print(line)
  return lines

def match_names():
  """
  Return: a list of movie titles
  that appear in both Cornell corpus and Bechdeltest.com
  """
  with open("movie_meta.json", "r") as handle:
    bechdel = json.load(handle)
    title_map = {}
    for each in bechdel:
      title = each['title'].lower()
      title_map[title] = each
  items = parse_txt("cornell_movie_dialogs_corpus/movie_titles_metadata.txt")

  type_cnt = {i:0 for i in range(4)}
  matched = []
  for item in items:
    title = item[1].lower()
    if title in title_map:
      matched += title,
      type_cnt[int(title_map[title]['rating'])] += 1
  print('matches: {} / {}'.format(len(matched), len(items)))
  for i in range(4):
    print('#{}: {}'.format(i, type_cnt[i]))
  return matched

def get_lines():
  """
  Return:
    mid_map: a dict of movie ids (mid).
    mid_map[mid] = {'convs': [conversations], 'lines':[lines]}
  """
  items = parse_txt('cornell_movie_dialogs_corpus/movie_conversations.txt')
  mid_map = {}
  for item in items:
    mid, lids = item[2], item[3]
    lids = [each[1:-1] for each in lids[1:-1].split(', ')]
    if mid not in mid_map:
      mid_map[mid] = {}
      mid_map[mid]['convs'] = []
      mid_map[mid]['lines'] = []
    mid_map[mid]['convs'] += lids,
    mid_map[mid]['lines'] += lids
  return mid_map

def title_to_mid():
  """
  Return: a dict from movie title to movie id (mid)
  """
  items = parse_txt("cornell_movie_dialogs_corpus/movie_titles_metadata.txt")
  title_map = {}
  for item in items:
    mid, title = item[:2]
    title_map[title] = mid
  return title_map
 
def matched_lines(titles, mid_to_cnt):
  """
  Return: total_convs / total_lines: lists of aggregated conversations / lines
  Also print out number of conversations / lines in movies (specified by `titles`)
  """
  title_map = title_to_mid()
  total_convs, total_lines = [], []
  for title in titles:
    mid = title_map[title]
    total_convs += mid_to_cnt[mid]['convs']
    total_lines += mid_to_cnt[mid]['lines']

  print('{} convs & {} lines in {} movies'.format(len(total_convs), len(total_lines), len(titles)))
  return total_convs, total_lines

def parse_names(fname):
  """
  Return: a set of names; female or male
  """
  with open(fname, 'r') as fin:
    names = [line.strip().lower() for line in fin]
  return set(names)

def get_female_char_map():
  """
  Return:
    char_map: a dict of movie ids (mid).
    char_map[mid] is a list of ids of all female characters in the movie.
  """
  items = parse_txt('cornell_movie_dialogs_corpus/movie_characters_metadata.txt')
  char_map = {}
  female_names = parse_names('names_female.txt')
  for item in items:
    uid, name, mid, title, gender, pos = item
    if gender == '?' and name.lower() in female_names:
      gender = 'f'
    if gender == 'f':
      if mid not in char_map:
        char_map[mid] = []
      char_map[mid] += uid,
  return char_map

def line_to_gender(female_char_map):
  items = parse_txt('cornell_movie_dialogs_corpus/movie_lines.txt')
  line_map = {}
  for item in items:
    lid, uid, mid, name, line = item
    line_map[lid] = (1 if mid in female_char_map and uid in female_char_map[mid] else 0, '{}: {}'.format(name, line))
  return line_map

def filter_conv_by_gender(convs, line_map):
  labeled = {i:[] for i in range(3)}
  filtered = []
  failed = []
  for conv in convs:
    num_females = sum([line_map[lid][0] for lid in conv])
    if num_females > 1:
      filtered += [(lid, line_map[lid]) for lid in sorted(conv)],
    else:
      failed += [(lid, line_map[lid]) for lid in sorted(conv)],
  print('#filtered convs:', len(filtered))
  with open('filtered_conv.pkl', 'wb') as handle:
    pickle.dump(filtered, handle)
  with open('failed_conv.pkl', 'wb') as handle:
    pickle.dump(failed, handle)
  return filtered, failed
 
if __name__ == '__main__':
  matched_titles = match_names()
  mid_map = get_lines()
  total_convs, total_lines = matched_lines(matched_titles, mid_map)
  print()
  char_map = get_female_char_map()
  line_map = line_to_gender(char_map)
  filtered, failed = filter_conv_by_gender(total_convs, line_map)
