class Sequence:
    def __init__(self):
        self.totalSeq = ""
        self.id = ""
        self.leftUTR = ""
        self.codingSeq = []
        self.rightUTR = ""
        self.codonResults = []
        self.nucleotideResults = []

    def id_retrieve(self, total_line):
        """Obtains ID of sequence from first line of the tkinter text box submission"""
        split_line = total_line.split(" ", 1)[0]
        self.id = split_line[1:]

    def seq_format(self, string_seq):
        """Formats the tkinter text box submission"""
        self.totalSeq = "".join(string_seq)
        self.totalSeq = self.totalSeq.replace('\n', '')

    def find_start_stop(self):
        """Finds the start and stop codon of given sequence"""
        # Finding start codon
        first_split = self.totalSeq.split("ATG", 1)
        first_split[1] = "ATG" + first_split[1]
        self.leftUTR = first_split[0]

        # Finding stop codon
        remaining_seq = first_split[1]
        stop_codons = ["TAA", "TAG", "TGA"]
        for i in range(-1, len(remaining_seq), 3):
            curr_codon = remaining_seq[i+1:i+4]
            if curr_codon in stop_codons:
                self.rightUTR = remaining_seq[i+1:]  # Sets right UTR to remaining DNA.
                break
            else:
                self.codingSeq.append(curr_codon)
        # print(f"left UTR: {self.leftUTR}\ncoding Seq: {self.codingSeq}\nright UTR: {self.rightUTR}")
        # print(len(self.codingSeq))
