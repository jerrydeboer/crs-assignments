text = "X-DSPAM-Confidence:    0.8475";

chrpos = text.find(".")
chrlen = len(text)
chrnum = text[chrpos-1:chrlen]
print float(chrnum)
