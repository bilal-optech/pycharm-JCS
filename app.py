from nicegui import ui


def create_directory():
    ui.notify("Directory Created")


def load_directory():
    ui.notify("Directory Loaded")


def start_test(test_name):
    ui.notify(f"{test_name} Started")


def main():
    ui.markdown("## ILS Measurement Automation")

    with ui.row():
        ui.label("Working directory :")
        ui.input("Enter working directory")
        ui.button("Create directory", on_click=create_directory)
        ui.button("Load directory", on_click=load_directory)

    with ui.row():
        ui.label("Laser ID :")
        ui.input("Enter Laser ID")
        ui.button("Create directory", on_click=create_directory)
        ui.button("Load directory", on_click=load_directory)

    with ui.row():
        ui.label("Meas. Run Name :")
        ui.input("Enter Measurement Run Name")
        ui.button("Create directory", on_click=create_directory)
        ui.button("Load directory", on_click=load_directory)

    ui.markdown("### Test Menu")

    with ui.row():
        ui.label("Mechanical Shutter :")
        ui.button("Start", on_click=lambda: start_test("Mechanical Shutter"))
        ui.label("Status : Finished")

    with ui.row():
        ui.label("LT Power Monitoring :")
        ui.button("Start", on_click=lambda: start_test("LT Power Monitoring"))
        ui.number(value=7)
        ui.label("Status : Running - Port 7")

    with ui.row():
        ui.label("LT PER Measurement :")
        ui.button("Start", on_click=lambda: start_test("LT PER Measurement"))
        ui.number(value=1)
        ui.label("Status : Start")

    ui.run()


if __name__ in {"__main__", "__mp_main__"}:
    main()
