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


class EngineeringHighlight(BaseModel):
    title: str
    description: str
    details: list[str]
    impact: str | None = None
    url: str | None = None
    viewer_url: str | None = None
    

class Profile(BaseModel):
    identity: Identity
    robot_identity: RobotIdentity
    engineering_domains: EngineeringDomains
    learning: Learning
    engineering_highlights: list[EngineeringHighlight]