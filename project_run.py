from project_functions import calc_sym_words_ratio, calc_words_sent_ratio

u_text=input("Hello, please, enter the text to get useful statistics on it!\n")
symb_res=calc_sym_words_ratio(u_text)
sent_res=calc_words_sent_ratio(u_text)
if symb_res is None or sent_res is None:
    print("Sorry, you did not enter valid input, so I cannot provide you with the statistics on your input!")
else:
    print(f"On average, there are {symb_res} characters per word in your text.\nOn average there are {sent_res} words per sentence in your text")
