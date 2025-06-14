import inspect
from typing import Optional, Sequence


class PlotMixin:
    """
    Mixin to convert hte explaination to a plot.
    """

    def plot(self, *plot_method_args, package: Optional[str] = None, **plot_method_kwargs):
        """
        Plot the explaination using the requested library if available, otherwise raise a ValueError
        """
        # Get all methods defined in the class
        methods = inspect.getmembers(self, predicate=inspect.ismethod)

        # Filter for methods starting with 'plot_' excluding 'plot' itself
        plot_methods = [name for name, _ in methods if name.startswith("plot_") and name != "plot"]

        if not plot_methods:
            raise ValueError("No plotting methods defined!")

        if package and "plot_" + package in plot_methods:
            getattr(self, "plot_" + package)(*plot_method_args, **plot_method_kwargs)
        elif package is None:
            getattr(self, plot_methods[0])(*plot_method_args, **plot_method_kwargs)
        else:
            raise ValueError("No method defined to plot with the requested method!")

    def get_available_packages(self) -> Sequence[str]:
        """
        Retuens a list with the available packages for the explaination plot
        """
        methods = inspect.getmembers(self, predicate=inspect.ismethod)
        return [name[5:] for name, _ in methods if name.startswith("plot_") and name != "plot"]
