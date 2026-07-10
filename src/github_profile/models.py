from pydantic import BaseModel


class Identity(BaseModel):
    name: str
    title: str
    tagline: str
    location: str
    languages: list[str]


class RobotIdentity(BaseModel):
    enabled: bool = True
    mission: str


class EngineeringDomains(BaseModel):
    enabled: bool = True
    robotics: list[str]
    computer_vision: list[str]
    embedded_systems: list[str]
    software: list[str]
    infrastructure: list[str]


class Learning(BaseModel):
    enabled: bool = True
    topics: list[str]


class Profile(BaseModel):
    identity: Identity
    robot_identity: RobotIdentity
    engineering_domains: EngineeringDomains
    learning: Learning