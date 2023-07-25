# geolite2 query
## get ASN from IP


## Pending to do

- Automate db download and extraction on server startup
- Dockerise

## Examples

```sh
curl http://localhost:5000/geolocate?ip=1.1.1.1
{
  "autonomous_system_number": 13335,
  "autonomous_system_organization": "CLOUDFLARENET",
  "ip_address": "1.1.1.1",
  "prefix_len": 24
}
```