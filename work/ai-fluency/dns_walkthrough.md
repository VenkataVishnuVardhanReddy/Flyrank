# Domain Setup & DNS Walkthrough

This document contains the plain-English DNS walkthrough explaining how the internet routes users to your portfolio, preparing us for the custom FlyRank subdomain mapping at the end of the track.

---

## 1. Deployed Portfolio URL
Your portfolio research paper and safety consoles website is live over HTTPS at:
> **[https://venkatavishnuvardhanreddy.github.io/Flyrank/](https://venkatavishnuvardhanreddy.github.io/Flyrank/)**

---

## 2. Plain-English DNS Walkthrough (How the Internet Finds Your Site)

Imagine the internet is a massive international telephone network. Computers don't communicate using names like `flyrank.ai`; they communicate using number sequences called **IP addresses** (e.g., `185.199.108.153`). 

The **Domain Name System (DNS)** is the global phonebook that translates human-friendly website names into computer-friendly numbers.

Here is exactly what happens when someone types your custom address into a browser:

```text
 [User Browser] ────(1) "Where is vishnu.flyrank.ai?" ────► [DNS Resolver]
       ▲                                                           │
       │                                                           ├──(2) "Ask Nameserver..."
       │                                                           ▼
       │                                                    [Nameserver]
       │                                                           │
       └────(4) IP Address: 185.199.108.153 ◄────(3) Response ─────┘
```

### The 4-Step Connection Journey
1. **The Resolver (The Operator):** When a user types `vishnu.flyrank.ai`, the browser asks the local **DNS Resolver** (usually run by their internet provider or Google): *"Do you know where vishnu.flyrank.ai is?"*
2. **The Nameserver (The Directory Office):** If the Resolver doesn't have it saved, it queries the **Nameserver** (the authority server holding the official registry records for `flyrank.ai`). 
3. **The CNAME Record (The Forwarding Address):** The Nameserver looks up your specific entry. Since we set up a custom subdomain, it finds a **CNAME (Canonical Name) Record**. 
   - *What a CNAME is:* A CNAME is a "forwarding address" in the phonebook. Instead of pointing directly to an IP number, it says: *"This name is an alias for another name. Go look up `venkatavishnuvardhanreddy.github.io` instead."*
4. **The Response & Connection:** The Resolver does a quick lookup for `venkatavishnuvardhanreddy.github.io`, gets the IP address of GitHub's hosting servers, and returns it to the user's browser. The browser connects to that IP, downloads the HTML files, and displays the page.

---

## 3. Custom Domain Checklist (For Capstone Graduation)

When your custom FlyRank subdomain (e.g., `vishnu.flyrank.ai`) is provisioned at graduation, we will run this checklist to connect it:

1. **Ops Configuration (Their Half):** FlyRank Operations creates the DNS record mapping `vishnu.flyrank.ai` to point to `venkatavishnuvardhanreddy.github.io` on their DNS server.
2. **GitHub Pages Configuration (Your Half):**
   - Go to your repository settings on GitHub.
   - Click the **Pages** tab on the left.
   - Under **Custom domain**, type your subdomain (e.g., `vishnu.flyrank.ai`) and click **Save**.
3. **Wait for Propagation:** Wait 5–10 minutes for global DNS servers to update.
4. **Enforce HTTPS:** Once the CNAME resolves, tick **Enforce HTTPS** in GitHub Pages settings to generate the secure padlock certificate.
