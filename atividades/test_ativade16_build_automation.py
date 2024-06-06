import pytest
from python.atividades.atividade16_build_automation import automation_build, AutomationModel, RobotModel, StatusEnum, InstallationEnum

def test_automation_build_no_robots():
    # Arrange
    automation = AutomationModel(id=1, name="Test Automation", status=StatusEnum.RUNNING.value)
    robots = []

    # Act
    result = automation_build(automation_id=automation.id)

    # Assert
    assert result == f'Automation {automation.name} has no robots to execute.'

def test_automation_build_all_robots_installed():
    # Arrange
    automation = AutomationModel(id=1, name="Test Automation", status=StatusEnum.RUNNING.value)
    robots = [
        RobotModel(id=1, automation_id=automation.id, installed=InstallationEnum.INSTALLED.value),
        RobotModel(id=2, automation_id=automation.id, installed=InstallationEnum.INSTALLED.value),
        RobotModel(id=3, automation_id=automation.id, installed=InstallationEnum.INSTALLED.value)
    ]

    # Act
    result = automation_build(automation_id=automation.id)

    # Assert
    assert result == f'Automation {automation.name} builded successfully'

def test_automation_build_some_robots_not_installed():
    # Arrange
    automation = AutomationModel(id=1, name="Test Automation", status=StatusEnum.RUNNING.value)
    robots = [
        RobotModel(id=1, automation_id=automation.id, installed=InstallationEnum.INSTALLED.value),
        RobotModel(id=2, automation_id=automation.id, installed=InstallationEnum.NOT_INSTALLED.value),
        RobotModel(id=3, automation_id=automation.id, installed=InstallationEnum.INSTALLED.value)
    ]

    # Act
    result = automation_build(automation_id=automation.id)

    # Assert
    assert result == f'there is robots to install, building automation {automation.id} again'

# Run the tests
pytest.main()