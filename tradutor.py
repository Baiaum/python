#!/usr/bin/python
from googletrans import *;

tras = Translator()

input = "Eu estou tentando usar essa biblioteca";

src = "en";
trg = "pt";

translation = tras.translate("Eu estou traduzindo do português para o inglês")

print(f"Tradução: {translation.text}")