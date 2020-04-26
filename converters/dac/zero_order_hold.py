from scipy.interpolate import interp1d

from converters.dac.order_holder_converter import OrderHolderConverter


class ZeroOrderHoldConverter(OrderHolderConverter):

    def get_interpolation_function(self, x_values, y_values):
        return interp1d(x_values, y_values, kind='zero')
