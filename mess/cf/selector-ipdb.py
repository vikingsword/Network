# !usr/bin/env python
# -*- coding:utf-8 _*-
import requests

# Cloudflare API参数
api_token = "rwcQDmQYT4ioLUbh-iTKBhLqM7gjXci_a6s-fS1x"  # api key
zone_id = "e96bef8e3fdc518e41361fddcc0b519f"
domain = "selector.1593570.xyz"  # 您的二级域名

# Cloudflare API端点
api_url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"

# 请求标头
headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}


# 删除指定二级域名下的所有 DNS 记录
def delete_all_dns_records():
    response = requests.get(api_url, headers=headers, params={"name": domain})
    if response.status_code == 200:
        result = response.json()
        dns_records = result["result"]
        dns_record_ids = [record["id"] for record in dns_records]

        for record_id in dns_record_ids:
            delete_response = requests.delete(f"{api_url}/{record_id}", headers=headers)
            if delete_response.status_code == 200:
                print(f"已删除 DNS 记录: {record_id}")
            else:
                print(f"删除 DNS 记录时出错：{delete_response.text}")
    else:
        print("获取 DNS 记录时出错：", response.text)


# 获取优选 IP 数据并筛选延迟最低的 3 个数据
def fetch_and_filter_ips():
    url = "https://ipdb.api.030101.xyz/?type=bestproxy"
    resp = requests.get(url).text.strip()
    return resp.split("\n")


# 将筛选后的 IP 地址解析到 Cloudflare 域名下
def add_dns_records(ip_addresses):
    for ip_address in ip_addresses:
        data = {
            "type": "A",
            "name": domain,
            "content": ip_address,
            "ttl": 1,
            "proxied": False
        }
        response = requests.post(api_url, headers=headers, json=data)
        if response.status_code == 200:
            print(f"IP地址 {ip_address} 已成功解析到 Cloudflare 域名下")
        else:
            print(f"解析IP地址 {ip_address} 时出错：{response.text}")


# 主函数
def main():
    delete_all_dns_records()
    ip_addresses = fetch_and_filter_ips()
    if ip_addresses:
        add_dns_records(ip_addresses)
        print("所有操作已完成")
    else:
        print("没有符合条件的 IP 地址")


if __name__ == "__main__":
    main()
