def test(case_types):
	testinput={}

	if (case_types == 'hindi'):
		testinput = {"हिन्दी" : "हीन्दी", "घर": "घार", "घर": "घरम", "बाहर": "बहर", "अगर": "आरग"};
	elif (case_types == 'english'):
		testinput = {'correct': 'corect', 'in': 'iin', 'going': 'goin', 'see': 'cee'};
	elif(case_types == 'special'):
		testinput = {'don\'t': 'dont\'t', "come": "comes comin", 'won\'t': 'woo\'nt'};
	return testinput
