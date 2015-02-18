#!/usr/bin/python
# -*- coding: utf-8 -*-

#########################################################
#														#
#		Escrito por Antonio Carlos Falcão Petri			#
#					BCC-014, UFSCar						#
#														#
#########################################################

# Automatic test cases flag
testing = False

answer_message = 'MDC({0}, {1}) = {3} * {0} + {4} * {1} = {2}'
indice_message = '({0})'
steps_message = '{0:{width1}}/{1:<{width2}} = {2} resta {3}'
implies_message = ' => '
coefficients_expression = '{3} = {4} * {0} + {2} * {1}'

def euclid (a, b):
	values = []
	pairs = {}

	count = 1

	a_len = len(str(a))
	b_len = len(str(b))

	print 'Calculando MDC({0}, {1}):'.format(a,b)
	while b != 0:
		if values:
			v = { 'a':a, 'b':b, 'div':a/b, 'resto':a%b, 'alfa':1, 'beta':-values[-1]['resto'] }
		else:
			v = { 'a':a, 'b':b, 'div':a/b, 'resto':a%b, 'alfa':1, 'beta':-(a/b) }
		
		left, right = coefficients_expression.format \
			(v['alfa'], v['beta'], v['div'], v['resto'],
			 	v['a']).split(' = ')

		print indice_message.format(count) + '\t' + \
			steps_message.format( v['a'], v['b'], v['div'], v['resto'], 
				width1=a_len, width2=b_len)
		
		a, b = b, a%b

		if b != 0:
			values.append(v)
			pairs[left] = right
			count += 1

	mdc = a

	print
	print
	count = 1

	if values:
		v = values[0]
		v['div'] = v['b']

		left, right = coefficients_expression.format \
			(v['alfa'], v['beta'], v['div'], v['resto'],
			 	v['a']).split(' = ')
		pairs[left] = right
	
	for i in range(0, len(values)):
		v = values[i]

		print indice_message.format(count) + implies_message + \
			coefficients_expression.format(
				v['alfa'], v['beta'], v['div'], v['resto'], v['a']
			)

		if i != 0:
			if str(abs(v['a'])) in pairs or str(abs(v['beta'])) in pairs:
				expression_modified = coefficients_expression
				
				if str(abs(v['a'])) in pairs:
					expression_modified = expression_modified.format(
							v['alfa'], v['beta'], v['div'], v['resto'], v['a']
						).replace(str(v['a'])+' * ', '('+pairs[str(abs(v['a']))]+') * ' )
					
				if str(abs(v['beta'])) in pairs:
					expression_modified = expression_modified.format(
							v['alfa'], v['beta'], v['div'], v['resto'], v['a']
						).replace(' * '+str(v['beta']), ' * -('+pairs[str(abs(v['beta']))]+')' )
					

				print ' '*3 + implies_message + expression_modified

			if i == 1:
				v['alfa'] = 0 - values[i-1]['alfa'] * values[i]['div']
				v['beta'] = 1 - values[i-1]['beta'] * values[i]['div']
			else:
				v['alfa'] = values[i-2]['alfa'] - values[i-1]['alfa'] * values[i]['div']
				v['beta'] = values[i-2]['beta'] - values[i-1]['beta'] * values[i]['div']

			v['a'] = values[i-1]['a']
			v['div'] = values[i-1]['b']

			left, right = coefficients_expression.format \
				(v['alfa'], v['beta'], v['div'], v['resto'],
			 		v['a']).split(' = ')
			pairs[left] = right

			print ' '*3 + implies_message +  \
				coefficients_expression.format(
					v['alfa'], v['beta'], v['div'], v['resto'], v['a']
				)

		count += 1
		print

	if values:
		alfa, beta = values[-1]['alfa'], values[-1]['beta']
	else:
		alfa = (0 if a == 0 else 1)
		beta = int(not alfa)

	return mdc, alfa, beta	

def get_input ():
	while True: 
		try:
			n1 = int(raw_input('Digite o primeiro numero: '))
			n2 = int(raw_input('Digite o segundo número: '))
			
			if n1 < 0 or n2 < 0:
				raise ValueError('Não sei calcular o MDC de números negativos.\n'
					'Tente usar essa relação: MDC({0}, {1}) = MDC({2}, {3}).'.format(n1, n2, abs(n1), abs(n2)))

			return (n1, n2) if (n1 > n2) else (n2, n1)
		except ValueError as e:
			print
			print str(e)
			print

def show_answer (n1, n2):
	print
	print
	mdc, alfa, beta = euclid(n1, n2)

	print answer_message.format(n1, n2, mdc, alfa, beta)

def main ():
	if testing:
		tests = [ [32, 76], [76, 92], [15, 69], [29, 83], [96, 11], [77, 55]]

		for test in tests:
			n1, n2 = test
			show_answer(n1, n2)
	else:
		n1, n2 = get_input()
		show_answer(n1, n2)

if __name__ == '__main__':
	main()
