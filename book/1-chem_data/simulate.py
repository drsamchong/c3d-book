import numpy as np
from typing import Sequence, Callable

def simulate_peak(peak_fn, x_array, ampl, centre, width):
    calc_peak = peak_fn(x_array, ampl, centre, width)
    sim_peak = [y+np.random.normal(0, 0.05) for y in calc_peak]
    return sim_peak

def simulate_spectrum(peak_fn: Callable, x_array: Sequence[float], peaks: list[dict], add_noise=False) -> tuple[np.ndarray, np.ndarray]:
    #x_array = np.linspace(x_range[0], x_range[1], abs(x_range[0]-x_range[1])*100)
    y_array = np.zeros(len(x_array))
    for peak in peaks:
        calc_peak = peak_fn(x_array, peak["ampl"], peak["centre"], peak["width"])
        y_array = y_array + calc_peak
    if add_noise:    
        y_array = [y+np.random.normal(0, 0.05) for y in y_array]
    return x_array, y_array

