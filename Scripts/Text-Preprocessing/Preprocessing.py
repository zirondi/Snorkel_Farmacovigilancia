# os: _get_files, toEventsDicio
import os

# shutil: _get_files
from shutil import copy

# nltk.corpus: _to_drugs_dict, _to_events_dict
from nltk.corpus import stopwords


class Util:
    def __init__(self, input_path, output_path, command=True):

        self.divisor = os.path.sep
        self.input_path = input_path
        self.output_copy_path = output_path + f"{self.divisor}toBeProcessed{self.divisor}"
        self.output_path = output_path + f"{self.divisor}Processed{self.divisor}"

        if command == True:
            # List order matters
            self.white_list = [
                "Eventos.txt",
                "EventosAdversos-gazette.txt",
                "Remédios-br-gazette.txt",
                "Substâncias-br-gazette.txt",
                "Tweets Anotados.txt",
                "Remédios2-br-gazette.txt",
                "Substâncias2-br-gazette.txt",
            ]
            self._get_files()
            self._to_tsv()
            self._to_drugs_dict()
            self._to_events_dict()

    # Copying files listed in whitelist, from input_path to output_path
    def _get_files(self):

        if not os.path.exists(self.output_copy_path):
            os.makedirs(self.output_copy_path)

        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

        for r, _, f in os.walk(self.input_path, topdown=True):
            for files in f:
                if files in self.white_list:
                    copy(os.path.join(r, files), self.output_copy_path)
                    print("File %s was successfully copied" % files)

    # Creating the .tsv from 'Tweets Anotatos.txt'
    def _to_tsv(self):
        txt = open(
            self.output_copy_path + self.divisor + self.white_list[4],
            "r",
            encoding="UTF-8",
        )
        tsv = open(
            self.output_path + self.divisor + self.white_list[4].replace("txt", "tsv"),
            "w",
            encoding="UTF-8",
        )

        tsv.write("Index" + "\t" + "Tweet" + "\n")
        i = 0

        for line in txt:
            if 'http' not in text and 'https' not in text and 'pic twitter' not in text:
                tsv.write(
                    str(i)
                    + "\t"
                    + line.lower().replace("\n", "").replace(" ", "", 1)
                    + "\n"
                )
                i += 1

        tsv.close()
        txt.close()
        print(".tsv Corpus created successfully.")

    # Creating the .txt drugs dictionary
    def _to_drugs_dict(self):

        drug_dictionary = [
            self.white_list[2],
            self.white_list[3],
            self.white_list[5],
            self.white_list[6],
        ]
        dict_limiters = {
            self.white_list[2]: 6701,
            self.white_list[3]: 1778,
            self.white_list[5]: 5904,
            self.white_list[6]: 815,
        }

        final_set = set()

        for d in drug_dictionary:
            if d == self.white_list[5]:
                f = open(
                    self.output_copy_path + self.divisor + d, "r", encoding="UTF-16le"
                )
            else:
                f = open(
                    self.output_copy_path + self.divisor + d, "r", encoding="UTF-8"
                )
            s = f.read()
            f.close()

            s = s.replace("DRUG\t", "")
            s = s.replace("\t", " ")
            s = s.splitlines()

            for i in range(0, dict_limiters[d]):
                final_set.add(s[i].lower())

        stop_words = set(stopwords.words("portuguese"))
        final_set.difference_update(stop_words)
        final_list = sorted(final_set)

        txt = open(
            self.output_path + self.divisor + "Dicionario_de_Substancias.txt",
            "w",
            encoding="UTF-8",
        )

        for line in final_list[:-1]:
            txt.write(line + "\n")
        txt.close()
        print(".txt Drugs Dictionary created successfully.")

    # Creating the .txt events dictionary
    def _to_events_dict(self):

        final_set = set()

        f = open(
            self.output_copy_path + self.divisor + self.white_list[0],
            "r",
            encoding="UTF-8",
        )
        s = f.read()
        f.close()

        s = s.splitlines()

        for line in s:
            final_set.add(line.lower())
        
        to_add = ['dor de estomago', 'dor no estomago', 'dor de barriga', 'dor na barriga']
        for word in to_add:
            final_set.add(word)
        
        final_set.remove('com calor')

        f = open(
            self.output_copy_path + self.divisor + self.white_list[1],
            "r",
            encoding="UTF-8",
        )
        s = f.read()
        f.close()

        s = s.replace("Event	", "")
        s = s.splitlines()

        for i in range(0, 11561):
            final_set.add(s[i].lower())

        to_remove = ['pro', 'anti', 'cloridrato', 'óleo']

        for word in to_remove:
            final_set.remove(word)
        
        final_set.add("sono")

        stop_words = set(stopwords.words("portuguese"))
        final_set.difference_update(stop_words)
        final_list = sorted(final_set)

        txt = open(
            self.output_path + self.divisor + "Dicionario_de_Eventos.txt",
            "w",
            encoding="UTF-8",
        )

        for line in final_list:
            txt.write(line + "\n")
        txt.close()
        print(".txt Events Dictionary created successfully.")

    # Returns the dictonaries as List()
    def drugs_to_list(self):

        f = open(
            self.output_path + self.divisor + "Dicionario_de_Substancias.txt",
            "r",
            encoding="UTF-8",
        )
        s = f.read()
        f.close()
        s = s.splitlines()

        return s

    def events_to_list(self):
        f = open(
            self.output_path + self.divisor + "Dicionario_de_Eventos.txt",
            "r",
            encoding="UTF-8",
        )
        s = f.read()
        f.close()
        s = s.splitlines()

        return s

    # Returnes the .tsv Corpus path
    def get_tsv_path(self):
        return (
            self.output_path + self.divisor + self.white_list[4].replace("txt", "tsv")
        )

