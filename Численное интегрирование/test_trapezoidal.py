def test_trapezoidal_one_exat_value():
	"""
	Тестирование на результатах, полученных в ручную
	"""
	from math import exp
	v = lambda x: 3*x**2*exp(x**3)
	n = 2
	expected = 3*(0.25**2*exp(0.25**3) + 0.75**2*exp(0.75**3))
	computed = trapezoidal(v, 0, 1, 2)
	rel_error = abs(expected - computed)
	tol = 1E-15
	success = rel_error < tol
	msg = 'погрешность = %.17f больше допуска = %.17f' % (rel_error, tol)
	assert success, msg 