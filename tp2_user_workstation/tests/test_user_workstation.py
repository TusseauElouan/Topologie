from tp2_user_workstation.python.user_workstation import User, Workstation


def test_full_name() -> None:
    user = User(first_name="Robert", last_name="CEO", department="Direction", role="CEO")
    assert user.full_name() == "Robert CEO"


def test_assign_workstation_updates_both_sides() -> None:
    user = User(first_name="Guillaume", last_name="IT", department="IT", role="Admin")
    workstation = Workstation(hostname="it-01", ip_address="192.168.21.10", os_name="Linux")

    user.assign_workstation(workstation)

    assert user.workstation is workstation
    assert workstation.owner is user

