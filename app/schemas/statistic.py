from pydantic import BaseModel


class StatisticCourseCodeModel(BaseModel):
    """
    Model for POST request to `/statistic/`
    """

    course_code: str = "МТ_Б2017_ИВТХ_2"


class ParticipantModel(BaseModel):
    """
    Describe participant response from Zoom API
    """

    id: str = "QiHAwlFoRE6Rt1FEsJ4XrQ"
    user_id: str = "16778240"
    user_name: str = "Игорь Бирюков"
    device: str = "Неизвестно"
    ip_address: str = "95.27.134.59"
    location: str = "Moscow (RU)"
    network_type: str = "Проводное соединение"
    data_center: str = "Германия (Cloud Верхний)"
    connection_type: str = "UDP"
    join_time: str = "2021-02-16T11:30:44Z"
    leave_time: str = "2021-02-16T12:47:00Z"
    share_application: bool = False
    share_desktop: bool = False
    share_whiteboard: bool = True
    recording: bool = True
    pc_name: str = "LAPTOP-JDD4MFUM"
    domain: str = ""
    mac_addr: str = ""
    harddisk_id: str = ""
    version: str = "5.4.59931.0110"
    leave_reason: str = (
        "Игорь Бирюков покинул (-а) конференцию."
        "<br>Причина:покинул (-а) конференцию."
    )
    email: str = "ibirjkov@miem.hse.ru"
    status: str = "in_meeting"


class StatisticResponseModel(BaseModel):
    """
    Describe response from Zoom API statistic request
    """

    page_count: int = 1
    page_size: int = 100
    total_records: int = 23
    next_page_token: str = ""
    participants: list[ParticipantModel]
