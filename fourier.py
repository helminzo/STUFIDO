import matplotlib.pyplot as plt
import numpy as np

# Fourier series for a function defined on any interval with equally spaced points
def fourier_series(x, y, n=None):
    if n is None:
        n = x.shape[0]//2
    num_pts = x.shape[0] #The number of evenly spaced points to evaluate 
    domain_width = x[-1] - x[0]
    dx = np.ones(num_pts)*domain_width/num_pts
    f0 = 2*np.pi/domain_width #Fundamental frequency
    a0 = (y @ dx)/(domain_width)
    a_sines = []
    a_cosines = []
    for i in range(1, n+1):
        as_i = (y*np.sin(f0*i*x))@dx/(domain_width/2)
        ac_i = (y*np.cos(f0*i*x))@dx/(domain_width/2)
        a_sines.append(as_i)
        a_cosines.append(ac_i)
    # Return the fundamental frequency, the constant coefficient,
    # the sine coefficients and the cosine coefficients
    return (f0, a0, a_sines, a_cosines)

def slow_ft(x_lims, y): # x_lim is a list specifying the two endpoints of the domain [x_1, x_2], y is the array of function values
    n = len(y)
    omega_cos = np.cos(2*np.pi/n)
    omega_sin = np.sin(2*np.pi/n)
    #TODO: complete this slow fourier function.

def fourier_approx(x, coeffs): # Outputs the fourier approximation of some function defined by the coefficients 'coeffs' evaluated at 'x'
                               # 'coeffs' must be in the format of the output of the 'fourier_series' function
    ans = 0
    ans += coeffs[1]
    for i in range(len(coeffs[2])):
        ans += coeffs[2][i]*np.sin(coeffs[0]*(i+1)*x) + coeffs[3][i]*np.cos(coeffs[0]*(i+1)*x)
    return ans

def plot_diff_n_comps(x,y, num_waves = [1,10,100, 1000]):
    fig, ax = plt.subplots(2,2) 
    
    fourier_coeffs_0 = fourier_series(x, y, n=num_waves[0])
    fourier_coeffs_1 = fourier_series(x, y, n=num_waves[1])
    fourier_coeffs_2 = fourier_series(x, y, n=num_waves[2])
    fourier_coeffs_3 = fourier_series(x, y, n=num_waves[3])

    fig.suptitle('Fourier series of f(x) with n components')
    ax[0][0].plot(x, y, x, fourier_approx(x, fourier_coeffs_0))
    ax[0][0].set_title(f'n={num_waves[0]}')
    ax[0][1].plot(x, y, x, fourier_approx(x, fourier_coeffs_1))
    ax[0][1].set_title(f'n={num_waves[1]}')
    ax[1][0].plot(x, y, x, fourier_approx(x, fourier_coeffs_2))
    ax[1][0].set_title(f'n={num_waves[2]}')
    ax[1][1].plot(x, y, x, fourier_approx(x, fourier_coeffs_3))
    ax[1][1].set_title(f'n={num_waves[3]}')
    plt.show()

def plt_seriestransform(x, y, n=None):
    fig, ax = plt.subplots(1, 3)
    fourier_coeffs = fourier_series(x, y, n)
    ax[0].plot(x, y, x, fourier_approx(x, fourier_coeffs))
    ax[0].set_title(f'Fourier approx with n={len(fourier_coeffs[2])}')
    freqs = np.array(range(1, len(fourier_coeffs[2])+1))*fourier_coeffs[0]
    y_lim = [1.1*min(min(fourier_coeffs[2]), min(fourier_coeffs[3])), 1.1*max(max(fourier_coeffs[2]), max(fourier_coeffs[3]))]
    ax[1].plot(freqs, fourier_coeffs[2], 'bo', markersize=1)
    ax[1].set_ylim(y_lim)
    ax[1].set_title('Sine frequency amplitude')
    ax[2].set_ylim(y_lim)
    ax[2].plot(freqs, fourier_coeffs[3], 'bo', markersize=1)
    ax[2].set_title('Cosine frequency amplitude')
    plt.show()

x = np.linspace(-7,7, 1000)
y = 1/(1+np.exp(-x))
plt_seriestransform(x,y,150)