# Ortak Sonuç Şeması

Common baseline starter aşağıdaki alanları yazar. Alan adları intentionally English tutulur; bunun nedeni bütün grup sonuçlarını birleştirebilmek ve publication/reproducibility aşamasında sabit bir machine-readable şema kullanmaktır.

- `project_id`
- `scenario_id`
- `model_label`
- `standard`
- `band_ghz`
- `channel_width_mhz`
- `topology`
- `ap_placement`
- `n_sta`
- `distance_m`
- `path_loss_exponent`
- `reference_loss_db`
- `tx_power_dbm`
- `offered_load_mbps_per_sta`
- `packet_size`
- `enable_rts`
- `rate_manager`
- `data_mode`
- `mobility_speed_mps`
- `seed`
- `run`
- `simulation_time_s`
- `aggregate_throughput_mbps`
- `pdr_pct`
- `mean_delay_ms`
- `jain_fairness`

Specialized projeler project-specific metric ekleyebilir (ör. per-class delay veya per-BSS throughput); ancak daha sonra sonuçların birleştirilebilmesi için ortak identifying fields korunmalıdır.
