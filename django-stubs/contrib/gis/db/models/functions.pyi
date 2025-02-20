from typing import Any

from django.db.models import Func
from django.db.models import Transform as StandardTransform

NUMERIC_TYPES: Any

class GeoFuncMixin:
    geom_param_pos: Any
    @property
    def geo_field(self) -> Any: ...

class GeoFunc(GeoFuncMixin, Func): ...

class GeomOutputGeoFunc(GeoFunc):
    @property
    def output_field(self) -> Any: ...

class SQLiteDecimalToFloatMixin:
    def as_sqlite(self, compiler: Any, connection: Any, **extra_context: Any) -> Any: ...

class OracleToleranceMixin:
    tolerance: float
    def as_oracle(self, compiler: Any, connection: Any, **extra_context: Any) -> Any: ...

class Area(OracleToleranceMixin, GeoFunc):
    arity: int
    @property
    def output_field(self) -> Any: ...
    def as_sqlite(self, compiler: Any, connection: Any, **extra_context: Any) -> Any: ...

class Azimuth(GeoFunc):
    output_field: Any
    arity: int
    geom_param_pos: Any

class AsGeoJSON(GeoFunc):
    output_field: Any
    def __init__(
        self, expression: Any, bbox: bool = ..., crs: bool = ..., precision: int = ..., **extra: Any
    ) -> None: ...
    def as_oracle(self, compiler: Any, connection: Any, **extra_context: Any) -> Any: ...

class AsGML(GeoFunc):
    geom_param_pos: Any
    output_field: Any
    def __init__(self, expression: Any, version: int = ..., precision: int = ..., **extra: Any) -> None: ...
    def as_oracle(self, compiler: Any, connection: Any, **extra_context: Any) -> Any: ...

class AsKML(GeoFunc):
    output_field: Any
    def __init__(self, expression: Any, precision: int = ..., **extra: Any) -> None: ...

class AsSVG(GeoFunc):
    output_field: Any
    def __init__(self, expression: Any, relative: bool = ..., precision: int = ..., **extra: Any) -> None: ...

class AsWKB(GeoFunc):
    output_field: Any
    arity: int

class AsWKT(GeoFunc):
    output_field: Any
    arity: int

class BoundingCircle(OracleToleranceMixin, GeomOutputGeoFunc):
    def __init__(self, expression: Any, num_seg: int = ..., **extra: Any) -> None: ...
    def as_oracle(self, compiler: Any, connection: Any, **extra_context: Any) -> Any: ...

class Centroid(OracleToleranceMixin, GeomOutputGeoFunc):
    arity: int

class Difference(OracleToleranceMixin, GeomOutputGeoFunc):
    arity: int
    geom_param_pos: Any

class DistanceResultMixin:
    @property
    def output_field(self) -> Any: ...
    def source_is_geography(self) -> Any: ...

class Distance(DistanceResultMixin, OracleToleranceMixin, GeoFunc):
    geom_param_pos: Any
    spheroid: Any
    def __init__(self, expr1: Any, expr2: Any, spheroid: Any | None = ..., **extra: Any) -> None: ...
    def as_postgresql(self, compiler: Any, connection: Any, **extra_context: Any) -> Any: ...
    def as_sqlite(self, compiler: Any, connection: Any, **extra_context: Any) -> Any: ...

class Envelope(GeomOutputGeoFunc):
    arity: int

class ForcePolygonCW(GeomOutputGeoFunc):
    arity: int

class GeoHash(GeoFunc):
    output_field: Any
    def __init__(self, expression: Any, precision: Any | None = ..., **extra: Any) -> None: ...
    def as_mysql(self, compiler: Any, connection: Any, **extra_context: Any) -> Any: ...

class GeometryDistance(GeoFunc):
    output_field: Any
    arity: int
    function: str
    arg_joiner: str
    geom_param_pos: Any

class Intersection(OracleToleranceMixin, GeomOutputGeoFunc):
    arity: int
    geom_param_pos: Any

class IsValid(OracleToleranceMixin, GeoFuncMixin, StandardTransform):
    lookup_name: str
    output_field: Any
    def as_oracle(self, compiler: Any, connection: Any, **extra_context: Any) -> Any: ...

class Length(DistanceResultMixin, OracleToleranceMixin, GeoFunc):
    spheroid: Any
    def __init__(self, expr1: Any, spheroid: bool = ..., **extra: Any) -> None: ...
    def as_postgresql(self, compiler: Any, connection: Any, **extra_context: Any) -> Any: ...
    def as_sqlite(self, compiler: Any, connection: Any, **extra_context: Any) -> Any: ...

class LineLocatePoint(GeoFunc):
    output_field: Any
    arity: int
    geom_param_pos: Any

class MakeValid(GeomOutputGeoFunc): ...

class MemSize(GeoFunc):
    output_field: Any
    arity: int

class NumGeometries(GeoFunc):
    output_field: Any
    arity: int

class NumPoints(GeoFunc):
    output_field: Any
    arity: int

class Perimeter(DistanceResultMixin, OracleToleranceMixin, GeoFunc):
    arity: int
    def as_postgresql(self, compiler: Any, connection: Any, **extra_context: Any) -> Any: ...
    def as_sqlite(self, compiler: Any, connection: Any, **extra_context: Any) -> Any: ...

class PointOnSurface(OracleToleranceMixin, GeomOutputGeoFunc):
    arity: int

class Reverse(GeoFunc):
    arity: int

class Scale(SQLiteDecimalToFloatMixin, GeomOutputGeoFunc):
    def __init__(self, expression: Any, x: Any, y: Any, z: float = ..., **extra: Any) -> None: ...

class SnapToGrid(SQLiteDecimalToFloatMixin, GeomOutputGeoFunc):
    def __init__(self, expression: Any, *args: Any, **extra: Any) -> None: ...

class SymDifference(OracleToleranceMixin, GeomOutputGeoFunc):
    arity: int
    geom_param_pos: Any

class Transform(GeomOutputGeoFunc):
    def __init__(self, expression: Any, srid: Any, **extra: Any) -> None: ...

class Translate(Scale):
    def as_sqlite(self, compiler: Any, connection: Any, **extra_context: Any) -> Any: ...

class Union(OracleToleranceMixin, GeomOutputGeoFunc):
    arity: int
    geom_param_pos: Any
