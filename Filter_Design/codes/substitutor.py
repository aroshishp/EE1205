import sympy as sp

sl, s, z = sp.symbols('sl s z')

Ha_LP = 0.3125 / (sl**4 + 1.1068*sl**3 + 1.6125*sl**2 + 0.914*sl +0.3366)
sub = (s**2 + 0.7649**2)/(00.1247 * s)
new = Ha_LP.subs(sl, sub)
newsimp = sp.simplify(new)
print('Bandpass TF (unnormalized):')
print(newsimp)

# transfer function
Ha_BP_s = 7.55642e-5 * s**4 / (s**8 + 0.138015*s**7 + 2.36536*s**6 + 0.244019*s**5 + 2.08328*s**4 + 0.142769*s**3 + 0.809685*s**2 + 0.0276411*s + 0.117176)

# Here z denotes z^{-1}, for simplicity
substitution1 = ((1 - z) / (1 + z))
substituted_expression = Ha_BP_s.subs(s, substitution1)
simplified_expression = sp.simplify(substituted_expression)
print("\nDigital TF:")
print(simplified_expression)