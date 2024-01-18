-- 3. Old school band
select band_name, coalesce(split - formed, 0) as lifespan
from metal_bands
order by lifespan desc;
