# (http) envoy_inbound_read, envoy_inbound_userspace, envoy_inbound_write, 
# envoy_outbound_read, envoy_outbound_userspace, envoy_outbound_write
size_list = {"tcp":{100:[100, 241], 1000:[983, 1125], 2000:[1884, 2026], 3000:[2934, 3101], \
    4000:[3834, 4001]}, "http":{100:[100, 100, 252, 388, 388, 509], 1000:[983, 983, 1135, 1272, \
    1272, 1393], 2000:[1884, 1884, 2036, 2197, 2197, 2312], 3000:[2934, 2934, 3086, 3248, 3248, \
    3362], 4000:[3834, 3834, 3986, 4148, 4148, 4262], "http":{100:[134, 134, 160, 78, 78, 224], \
    1000:[1107, 1107, 1043, 961, 961, 1107], 2000:[1917, 19117, 1943, 1861, 1861, 2007], \
    3000:[2967, 2967, 2993, 2911, 2911, 3057], 4000:[3867, 3867, 3893, 3811, 3811, 3957]}}}