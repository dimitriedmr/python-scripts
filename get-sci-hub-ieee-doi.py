"""
Script gets IEEE STD 2003 DOIs from sci-hub database text file .

Document needed is IEEE Standard 181-2003 and contains information about waveforms.

https://knowledge.ni.com/KnowledgeArticleDetails?id=kA03q000000YNGZCA4&l=ro-RO
https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/vi-lib/measure/mascope-llb/transition-measurements-vi.html
IEEE Standard 181-2003, IEEE Standard on Transitions, Pulses, and Related Waveforms.

181-2003 https://ieeexplore.ieee.org/document/1245784 	DOI:10.1109/IEEESTD.2003.94394
181-1977 https://ieeexplore.ieee.org/document/29013 	DOI:10.1109/IEEESTD.1977.81097
194-1977 https://ieeexplore.ieee.org/document/29015 	DOI:10.1109/IEEESTD.1977.81098

https://en.wikipedia.org/wiki/Digital_object_identifier
https://sci-hub.se/
https://en.wikipedia.org/wiki/Library_Genesis
https://docs.python.org/3/library/codecs.html

output:
10.1109/ieeestd.2003.94243
10.1109/ieeestd.2003.94285
10.1109/ieeestd.2003.94395
10.1109/ieeestd.2003.94253
10.1109/ieeestd.2003.94230
10.1109/ieeestd.2003.6484221
10.1109/ieeestd.2003.94411
10.1109/ieeestd.2003.95605
10.1109/ieeestd.2003.6830795
10.1109/ieeestd.2003.94239
10.1109/ieeestd.2003.94241
10.1109/ieeestd.2003.94240
10.1109/ieeestd.2003.94251
10.1109/ieeestd.2003.94284
10.1109/ieeestd.2003.94408
10.1109/ieeestd.2003.94409
10.1109/ieeestd.2003.94238
10.1109/ieeestd.2003.248157
10.1109/ieeestd.2003.7116714
10.1109/ieeestd.2003.94249
10.1109/ieeestd.2003.94410
10.1109/ieeestd.2003.94388
10.1109/ieeestd.2003.7174934
10.1109/ieeestd.2003.6894722
10.1109/ieeestd.2003.8329043
10.1109/ieeestd.2003.6910350
10.1109/ieeestd.2003.94232
10.1109/ieeestd.2003.94237
10.1109/ieeestd.2003.94279
10.1109/ieeestd.2003.94228
10.1109/ieeestd.2003.94236
10.1109/ieeestd.2003.94283
10.1109/ieeestd.2003.94255
10.1109/ieeestd.2003.94245
10.1109/ieeestd.2003.94280
10.1109/ieeestd.2003.94392
10.1109/ieeestd.2003.94235
10.1109/ieeestd.2003.94391
10.1109/ieeestd.2003.94229
10.1109/ieeestd.2003.94384
10.1109/ieeestd.2003.94234
10.1109/ieeestd.2003.94252
10.1109/ieeestd.2003.94390
10.1109/ieeestd.2003.7508558
10.1109/ieeestd.2003.94247
10.1109/ieeestd.2003.94417
10.1109/ieeestd.2003.94385
10.1109/ieeestd.2003.339569
10.1109/ieeestd.2003.94248
10.1109/ieeestd.2003.339596
10.1109/ieeestd.2003.94393
10.1109/ieeestd.2003.94413
10.1109/ieeestd.2003.94254
10.1109/ieeestd.2003.94382
10.1109/ieeestd.2003.94407
10.1109/ieeestd.2003.94387
10.1109/ieeestd.2003.94394
10.1109/ieeestd.2003.94233
10.1109/ieeestd.2003.94383
10.1109/ieeestd.2003.94224
10.1109/ieeestd.2003.256915
10.1109/ieeestd.2003.94425
10.1109/ieeestd.2003.95617
10.1109/ieeestd.2003.94231
10.1109/ieeestd.2003.94282
10.1109/ieeestd.2003.94242
10.1109/ieeestd.2003.94386
10.1109/ieeestd.2003.94419
10.1109/ieeestd.2003.94281
10.1109/ieeestd.2003.94250
10.1109/ieeestd.2003.94412
10.1109/ieeestd.2003.94414
10.1109/ieeestd.2003.7840066
10.1109/ieeestd.2003.94389
10.1109/ieeestd.2003.8285455
10.1109/ieeestd.2003.94246
10.1109/ieeestd.2003.339580
10.1109/ieeestd.2003.94568
10.1109/ieeestd.2003.94244
"""

doi_sufix = "10.1109/ieeestd.2003"
doi_sufix_len = len(doi_sufix)
l = ""
path = r"dois-2022-02-12\sci-hub-doi-2022-02-12.txt"
with open(path, "r", encoding="iso8859_2") as pf:
	for l in pf:
		if doi_sufix == l[:doi_sufix_len]:
			print(l, end="")
