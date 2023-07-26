from pydantic import BaseModel, TypeAdapter, model_validator, ConfigDict
from typing import List, Optional

class FixturesModelItem(BaseModel):
    MatchNumber: int
    RoundNumber: int
    DateUtc: str
    Location: str
    HomeTeam: str
    AwayTeam: str
    Group: Optional[str]
    HomeTeamScore: int
    AwayTeamScore: int

    @model_validator(mode="after")
    def select_only_group_stages(self):
        if self.Group:
            return self.model_dump()

FixturesModel = TypeAdapter(list[FixturesModelItem])
