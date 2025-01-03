from typing import Dict, List, TypeVar, Generic, Optional, Any
from fastapi import UploadFile, File
from pydantic import BaseModel, Field

from all_types.response_dtypes import LyrInfoInCtlgSave

U = TypeVar("U")


class ReqModel(BaseModel, Generic[U]):
    message: str
    request_info: Dict
    request_body: U


class boxmapProperties(BaseModel):
    name: str
    rating: float
    address: str
    phone: str
    website: str
    business_status: str
    user_ratings_total: int


class ReqSavePrdcerLyer(BaseModel):
    prdcer_layer_name: str
    prdcer_lyr_id: str
    bknd_dataset_id: str
    points_color: str
    layer_legend: str
    layer_description: str
    city_name: str
    user_id: str


class ReqSavePrdcerCtlg(BaseModel):
    prdcer_ctlg_name: str
    subscription_price: str
    ctlg_description: str
    total_records: int
    lyrs: List[LyrInfoInCtlgSave] = Field(..., description="list of layer objects.")
    user_id: str
    # thumbnail_url: str
    display_elements: dict
    catalog_layer_options: dict


class ZoneLayerInfo(BaseModel):
    lyr_id: str
    property_key: str


class ReqCatalogId(BaseModel):
    catalogue_dataset_id: str


class ReqUserId(BaseModel):
    user_id: str


class Coordinate(BaseModel):
    latitude: float
    longitude: float


class ReqPrdcerLyrMapData(BaseModel):
    prdcer_lyr_id: str
    user_id: str


class ReqNearestRoute(ReqPrdcerLyrMapData):
    points: List[Coordinate]


class ReqFetchDataset(BaseModel):
    dataset_country: str
    dataset_city: str
    excludedTypes: list[str]
    includedTypes: list[str]
    action: Optional[str] = ""
    page_token: Optional[str] = ""
    search_type: Optional[str] = "default"
    text_search: Optional[str] = ""
    user_id: str


# class ReqApplyZoneLayers(BaseModel):
#     user_id: str
#     lyrs: List[str]
#     lyrs_as_zone: List[Dict[str, str]]


class ReqFetchCtlgLyrs(BaseModel):
    prdcer_ctlg_id: str
    as_layers: bool
    user_id: str


class ReqCostEstimate(BaseModel):
    included_categories: List[str]
    excluded_categories: List[str]
    city_name: str
    country: str


# Request models
class ReqLocation(BaseModel):
    lat: float
    lng: float
    radius: int
    excludedTypes: list[str]
    includedTypes: list[str]
    page_token: Optional[str] = ""
    text_search: Optional[str] = ""


class ReqRealEstate(BaseModel):
    country_name: str
    city_name: str
    excludedTypes: list[str]
    includedTypes: list[str]
    page_token: Optional[str] = ""
    text_search: Optional[str] = ""


class ReqCensus(BaseModel):
    country_name: str
    city_name: str
    includedTypes: List[str]
    page_token: Optional[str] = None


class ReqCommercial(BaseModel):
    country_name: str
    city_name: str
    includedTypes: List[str]
    page_token: Optional[str] = None
    

class ReqGradientColorBasedOnZone(BaseModel):
    color_grid_choice: list[str]
    change_lyr_id: str
    change_lyr_name:str
    based_on_lyr_id: str
    based_on_lyr_name:str
    coverage_value: float # [10min , 20min or 300 m or 500m]
    coverage_property: str #[Drive_time or Radius]
    color_based_on: str # ["rating" or "user_ratings_total"]


class ReqStreeViewCheck(BaseModel):
    lat: float
    lng: float
