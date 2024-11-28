from layout.components.pages.dashboard import Dashboard
import PySide6
def setup_dashboard(main_window, ui):
    # Getting Dashboard
    wrapper = Dashboard(main_window)
    ui.mainScroll.setWidget(wrapper)
    ui.gridLayout_2.addWidget(ui.mainScroll, 0, 0, 1, 1)