# flags = {
#     'ru': {'red blue', 'white'},
#     'kg': {'red yellow', 'red'},
#     'ua': {'red blue', 'red', 'blue'},
#     'uk': {'yellow', 'blue'},
#     'kz': {'blue yellow', 'blue'},
#     'us': {'red', 'white', 'blue'},
#     'de': {'black', 'red', 'yellow'},
#     'fr': {'blue', 'white', 'red'}
# }

# while True:
#   user_input = input("Введите цвета флагов (или 'выход' для завершения): ")

#   if user_input.lower() == 'выход':
#     print("Программа завершена.")
#     break

#   search_colors = set(user_input.lower().split())
#   found_domains = []

#   for domain, colors in flags.items():
#     all_flag_colors = set()
#     for c in colors:
#       for word in c.split():
#         all_flag_colors.add(word)

#     if search_colors.issubset(all_flag_colors):
#       found_domains.append(domain)

#   if found_domains:
#     print("Найденные домены:", found_domains)
#   else:
#     print("Доменов с такими цветами не найдено.")

d = []
n = []
b = []

for x in data_tuple:
  if isinstance(x, (list, tuple)):
    spisok = x
  else:
    spisok = [x]

  for s in spisok:
    if isinstance(s, bool):
      b.append(s)
    elif isinstance(s, int) or isinstance(s, float):
      n.append(s)
    elif isinstance(s, str):
      if s.isdigit():
        n.append(int(s))
      else:
        d.append(s)

noviy_n = []
for x in n:
  if x != 6.13:
    noviy_n.append(x)
n = noviy_n

for item in b:
  d.append(item)

try:
  ind_3 = n.index(3)
  ind_1 = n.index(1)
  maks_ind = max(ind_3, ind_1)
  n.insert(maks_ind, 2)
except:
  pass

n.sort(reverse=True)

d_rev = d[::-1]

d_final = []
for x in d_rev:
  if isinstance(x, str):
    d_final.append(x.swapcase())
  else:
    d_final.append(x)
d = d_final

print(n)
print(d)