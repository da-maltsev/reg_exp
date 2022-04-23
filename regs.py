import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код


class Reg_exp:

  def __init__(self, pattern_raw, pattern_new):
    self.pattern_raw = pattern_raw
    self.pattern_new = pattern_new

  def make_changes(self, contacts_list):
    contacts_list_upd = list()
    for card in contacts_list:
      card_as_string = ','.join(card)
      formatted_card = re.sub(self.pattern_raw, self.pattern_new, card_as_string)
      card_as_list = formatted_card.split(',')
      contacts_list_upd.append(card_as_list)
    return contacts_list_upd

  def join_duplicates(self, contacts_list):
    for i in contacts_list:
      for j in contacts_list:
        if i[0] == j[0] and i[1] == j[1] and i != j:
          if i[2] == '':
            i[2] = j[2]
          if i[3] == '':
            i[3] = j[3]
          if i[4] == '':
            i[4] = j[4]
          if i[5] == '':
            i[5] = j[5]
          if i[6] == '':
            i[6] = j[6]
    contacts_list_upd = list()
    for card in contacts_list:
      if card not in contacts_list_upd:
        contacts_list_upd.append(card)
    return contacts_list_upd

# Создаем переменные с регулярными выражениями
number_pattern_raw = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
                       r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
                       r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
number_pattern_new = r'+7(\4)\8-\11-\14\15\17\18\19\20'
name_pattern_raw = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
                     r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
name_pattern_new = r'\1\3\10\4\6\9\7\8'

# Создаем экзепляры класса для выполнения нужных преобразований
pretty_number = Reg_exp(number_pattern_raw, number_pattern_new)
correct_full_name = Reg_exp(name_pattern_raw, name_pattern_new)

# Используем методы класса для преобразований
if __name__ == '__main__':
  change_number = pretty_number.make_changes(contacts_list)
  change_name = correct_full_name.make_changes(change_number)
  no_duplicates = correct_full_name.join_duplicates(change_name)
  pprint(no_duplicates)

  # TODO 2: сохраните получившиеся данные в другой файл
  # код для записи файла в формате CSV
  with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(no_duplicates)