from project_functions import calc_sym_words_ratio

u_text=input("Hello, please, enter the text to get useful statistics on it!\n")
symb_res=calc_sym_words_ratio(u_text)
print(f"On average, there are {symb_res} characters per word in your text.")
