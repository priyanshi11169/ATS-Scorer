from typing import Any, Dict, List, Optional
from pydantic import BaseModel

class ComponentScores(BaseModel):
  formatting: float
  keywords : float
  content : float
  skill_validation : float
  ats_compatibility : float

# Resume VS JD Compariosn
class JDComparison(BaseModel):
  match_percentage : float
  semantic_similarity : float
  matched_keywords : List[str]
  missing_keywords : List[str]
  skills_gap : List[str]

# Skills that are proved from projects or not
class SkillValidationDetails(BaseModel):
  validated : List[Dict[str, Any]] = []
  unvalidated : List[str] = []
  total : int = 0
  validated_count: int = 0
  validation_pct : float = 0.0

# Problem where Resume Lacks and tips on improving it
class IssueDetail(BaseModel):
  issue_title : str
  severity_level : str
  ats_impact : str
  explanation : str
  where_it_appears : str
  how_to_fix : str
  action_items : List[str] = []
  example_improvement : str
  
class AnalysisResponse(BaseModel):
  # Final result that API will return to user
  
  # Main Score
  ATS_score : float
  component_scores : ComponentScores
  
  # Feedback
  issues_summary : List[str]
  detailed_feedback : List[IssueDetail]
  strengths : List[str] = []
  warnings : List[str] = []
  interpretation: str = ""
  
  # Skills that are fetched from resume
  skills : List[str] = []
  
  # Optinoal : When user also gives JD  
  jd_match_analysis : Optional[JDComparison] = None
  skill_validation_details : Optional[SkillValidationDetails] = None
  
  