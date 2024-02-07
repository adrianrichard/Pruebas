from tkinter import Tk, Toplevel, Frame, NSEW, Button, FLAT


class TKLegend:
    """
    Creates a legend sidebar to a TK window to edit buttons based on set criteria

    Parameters:
        root_window:
            Primary TK window to extend legend to
    """
    def __init__(self, root_window: Tk or Toplevel):
        """ Extension Attributes """
        self.root = root_window
        self.grid_row_start = root_window.grid_size()[1]
        self.column_count = root_window.grid_size()[0]

        """ Internal Functions"""
        self._modify_root_geometry()
        self._create_main_frame()
        self._create_legend_colors()

    def _modify_root_geometry(self):
        """ Modifies root window size to compensate for sidebar inclusion """
        self.root.minsize(width=803, height=700)

    def _create_main_frame(self):
        """ Create a frame for add event widgets """
        self.main_frame = Frame(self.root, bg=self.root["bg"])
        self.main_frame.grid(row=2, column=self.column_count, rowspan=self.grid_row_start, columnspan=2, sticky=NSEW)

    def _create_legend_colors(self):
        """ Creates button representation of colors with category text """
        colors = ["#F7D8BA", "#FEF8DD", "#C6B6D6", "#ACDDDE"]
        categories = ["Cody Works", "Sam Works", "Work Overlap", "Other"]
        for i, j in enumerate(colors):
            Button(self.main_frame, text=categories[i], bg=j, relief=FLAT).grid(row=i, column=0, sticky=NSEW, pady=25,
                                                                                padx=10)
