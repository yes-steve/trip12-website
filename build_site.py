# Builds the Trip 12 Future Foundation static site from shared templates.
import os

OUT = os.path.join(os.path.dirname(__file__), "site")
EMAIL = "info@trip12futurefoundation.org"  # PLACEHOLDER — replace when real inbox exists
EIN = "41-2611886"

LOGO = """<svg width="40" height="40" viewBox="0 0 48 48" role="img" aria-label="Trip 12 Future Foundation logo" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="tg1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E0218A"/><stop offset="50%" stop-color="#8B44E0"/><stop offset="100%" stop-color="#3D7BF7"/>
    </linearGradient>
    <linearGradient id="tg2" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3D7BF7"/><stop offset="55%" stop-color="#8B44E0"/><stop offset="100%" stop-color="#E0218A"/>
    </linearGradient>
  </defs>
  <rect x="1.5" y="1.5" width="45" height="45" rx="11" fill="#14141d" stroke="url(#tg1)" stroke-width="2"/>
  <path d="M16 5 C 34 15, 16 31, 33 43" fill="none" stroke="url(#tg1)" stroke-width="3.4" stroke-linecap="round"/>
  <path d="M32 5 C 14 15, 32 31, 15 43" fill="none" stroke="url(#tg2)" stroke-width="3.4" stroke-linecap="round"/>
  <rect x="20" y="10.6" width="8" height="2.4" rx="1.2" fill="#F7E44A"/>
  <rect x="20" y="22.8" width="8" height="2.4" rx="1.2" fill="#F7E44A"/>
  <rect x="20" y="35.2" width="8" height="2.4" rx="1.2" fill="#F7E44A"/>
</svg>"""

LOGO_SMALL = LOGO.replace('width="40" height="40"', 'width="30" height="30"')

NAV_ITEMS = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("programs.html", "Programs"),
    ("apply.html", "Apply for Assistance"),
    ("news.html", "News &amp; Events"),
    ("gallery.html", "Gallery"),
    ("get-involved.html", "Get Involved"),
    ("contact.html", "Contact"),
]

def header(active):
    items = []
    for href, label in NAV_ITEMS:
        cur = ' aria-current="page"' if href == active else ""
        items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    donate_cur = ' aria-current="page"' if active == "donate.html" else ""
    items.append(f'<li class="nav-cta"><a href="donate.html"{donate_cur}>Donate</a></li>')
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html">
      {LOGO}
      <span class="brand-name">Trip 12 Future Foundation<small>Hope for TRIP12 families</small></span>
    </a>
    <input type="checkbox" id="nav-toggle" class="nav-toggle" aria-hidden="true">
    <label for="nav-toggle" class="nav-toggle-label" aria-label="Open menu"><span></span></label>
    <nav class="site-nav" aria-label="Main navigation">
      <ul>
        {''.join(items)}
      </ul>
    </nav>
  </div>
</header>"""

FOOTER = f"""<footer class="site-footer">
  <div class="wrap">
    <div>
      <div class="footer-brand">{LOGO_SMALL} Trip 12 Future Foundation</div>
      <p>Financial assistance, support services, and educational resources for individuals and families affected by TRIP12-related disorders and related neurodevelopmental conditions.</p>
      <p>Clinton, Utah &middot; Serving families across the United States</p>
    </div>
    <div>
      <h4>Explore</h4>
      <ul>
        <li><a href="about.html">About the Foundation</a></li>
        <li><a href="programs.html">Our Programs</a></li>
        <li><a href="apply.html">Apply for Assistance</a></li>
        <li><a href="get-involved.html">Get Involved</a></li>
        <li><a href="news.html">News &amp; Events</a></li>
      </ul>
    </div>
    <div>
      <h4>Connect</h4>
      <ul>
        <li><a href="donate.html">Donate</a></li>
        <li><a href="contact.html">Contact Us</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-legal">
    <div class="wrap">Trip 12 Future Foundation Inc. is a 501(c)(3) tax-exempt public charity. EIN: {EIN}. Contributions are tax-deductible to the extent allowed by law. &copy; 2026 Trip 12 Future Foundation Inc. All rights reserved.</div>
  </div>
</footer>"""

def page(filename, title, description, body):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="stylesheet" href="css/style.css">
  <link rel="icon" type="image/svg+xml" href="img/favicon.svg">
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  {header(filename)}
  <main id="main">
{body}
  </main>
  {FOOTER}
</body>
</html>
"""
    with open(os.path.join(OUT, filename), "w") as f:
        f.write(html)
    print("wrote", filename)

ICON_HANDS = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#8b44e0" stroke-width="1.8" aria-hidden="true"><path d="M12 21s-7-4.6-9.5-8.5C.6 9.5 2 5.5 5.5 5.5c2 0 3.2 1.2 4 2.3.4.6 2.6.6 3 0 .8-1.1 2-2.3 4-2.3 3.5 0 4.9 4 3 7-2.5 3.9-7.5 8.5-7.5 8.5z"/></svg>'
ICON_DOG = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#8b44e0" stroke-width="1.8" aria-hidden="true"><path d="M4 16c0-4 3-7 8-7s8 3 8 7v3H4v-3z"/><circle cx="9" cy="6" r="2.4"/><circle cx="15" cy="6" r="2.4"/><path d="M9 19v-2m6 2v-2"/></svg>'
ICON_BOOK = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#8b44e0" stroke-width="1.8" aria-hidden="true"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15.5H6.5A2.5 2.5 0 0 0 4 21V5.5z"/><path d="M4 18.5A2.5 2.5 0 0 1 6.5 16H20"/></svg>'

def netlify_form(name, fields, button_label):
    """Netlify-detected static form with honeypot + thanks redirect."""
    return f"""<form name="{name}" method="POST" action="/thanks.html" data-netlify="true" netlify-honeypot="bot-field" class="form-card form-grid">
          <input type="hidden" name="form-name" value="{name}">
          <p class="hidden-field"><label>Don't fill this out: <input name="bot-field"></label></p>
{fields}
          <div><button type="submit" class="btn btn-primary">{button_label}</button></div>
        </form>"""

CONTACT_FORM = netlify_form("contact", f"""          <div class="form-row">
            <div class="field"><label for="c-name">Name</label><input type="text" id="c-name" name="name" required></div>
            <div class="field"><label for="c-email">Email</label><input type="email" id="c-email" name="email" required></div>
          </div>
          <div class="field"><label for="c-topic">Topic</label>
            <select id="c-topic" name="topic">
              <option>General question</option>
              <option>Donations</option>
              <option>Volunteering</option>
              <option>Press / partnership</option>
              <option>Other</option>
            </select>
          </div>
          <div class="field"><label for="c-message">Message</label><textarea id="c-message" name="message" required></textarea></div>""",
    "Send Message")

VOLUNTEER_FORM = netlify_form("volunteer", f"""          <div class="form-row">
            <div class="field"><label for="v-name">Name</label><input type="text" id="v-name" name="name" required></div>
            <div class="field"><label for="v-email">Email</label><input type="email" id="v-email" name="email" required></div>
          </div>
          <div class="field"><label for="v-city">City &amp; state <span class="hint">(optional)</span></label><input type="text" id="v-city" name="city_state"></div>
          <div class="field"><label for="v-help">How would you like to help?</label><textarea id="v-help" name="how_to_help" placeholder="Events, fundraising, outreach, professional skills, spreading the word..." required></textarea></div>""",
    "Sign Me Up")

APPLICATION_FORM = netlify_form("assistance-application", f"""          <div class="form-row">
            <div class="field"><label for="a-name">Your full name</label><input type="text" id="a-name" name="applicant_name" required></div>
            <div class="field"><label for="a-email">Email</label><input type="email" id="a-email" name="email" required></div>
          </div>
          <div class="form-row">
            <div class="field"><label for="a-phone">Phone <span class="hint">(optional)</span></label><input type="tel" id="a-phone" name="phone"></div>
            <div class="field"><label for="a-city">City &amp; state</label><input type="text" id="a-city" name="city_state" required></div>
          </div>
          <div class="field"><label for="a-relation">Your relationship to the affected individual</label>
            <select id="a-relation" name="relationship">
              <option>Parent or guardian</option>
              <option>I am the affected individual</option>
              <option>Other family member</option>
              <option>Caregiver or advocate</option>
            </select>
          </div>
          <div class="field"><label for="a-request">What assistance are you requesting?</label><textarea id="a-request" name="request_description" placeholder="Describe the therapy, equipment, treatment, or support you need help with." required></textarea></div>
          <div class="field"><label for="a-cost">Estimated cost <span class="hint">(if known)</span></label><input type="text" id="a-cost" name="estimated_cost" placeholder="e.g. $1,200 for 8 speech therapy sessions"></div>
          <div class="checkbox-field"><input type="checkbox" id="a-ack" name="documentation_acknowledged" required><label for="a-ack">I understand that medical documentation confirming a qualifying diagnosis and documentation of financial need will be required before an application can be reviewed, and that the Foundation will contact me with instructions for providing them securely.</label></div>""",
    "Submit Application")


# ---------------- HOME ----------------
home = f"""
    <div class="hero">
      <div class="wrap">
        <span class="eyebrow">A 501(c)(3) public charity &middot; Clinton, Utah</span>
        <h1>Hope and help for families facing TRIP12&#8209;related disorders</h1>
        <p class="lede">We provide direct financial assistance, service animal support, and education for individuals and families affected by the TRIP12 gene disorder and related neurodevelopmental conditions.</p>
        <div class="btn-row">
          <a class="btn btn-amber" href="donate.html">Donate</a>
          <a class="btn btn-secondary" href="apply.html">Apply for Assistance</a>
        </div>
      </div>
    </div>

    <section>
      <div class="wrap center">
        <h2>What we do</h2>
        <p class="section-intro">Rare genetic disorders bring extraordinary costs &mdash; therapies, equipment, and treatments that insurance doesn't fully cover. We help carry that weight.</p>
        <div class="card-grid" style="text-align:left">
          <div class="card">
            <div class="icon">{ICON_HANDS}</div>
            <h3>Financial Assistance</h3>
            <p>Direct help with medically necessary expenses not fully covered by insurance &mdash; specialist visits, therapies, adaptive equipment, and more. Paid directly to providers whenever possible.</p>
            <a class="more" href="programs.html#financial">Learn more &rarr;</a>
          </div>
          <div class="card">
            <div class="icon">{ICON_DOG}</div>
            <h3>Service Animal Support</h3>
            <p>Support for the placement, training, and care of service animals that assist individuals with neurological or developmental disabilities associated with genetic disorders.</p>
            <a class="more" href="programs.html#service-animals">Learn more &rarr;</a>
          </div>
          <div class="card">
            <div class="icon">{ICON_BOOK}</div>
            <h3>Education &amp; Awareness</h3>
            <p>Free educational materials, community awareness initiatives, and resource sharing for families and caregivers navigating TRIP12-related and similar rare conditions.</p>
            <a class="more" href="programs.html#education">Learn more &rarr;</a>
          </div>
        </div>
      </div>
    </section>

    <section class="alt">
      <div class="wrap">
        <div class="fact-strip">
          <div class="fact"><span class="num">501(c)(3)</span><span class="label">IRS-recognized public charity &mdash; donations are tax-deductible</span></div>
          <div class="fact"><span class="num">100%</span><span class="label">Volunteer board &mdash; no director or officer receives compensation</span></div>
          <div class="fact"><span class="num">Direct-to-provider</span><span class="label">Assistance is paid straight to clinics, therapists, and vendors</span></div>
          <div class="fact"><span class="num">Nationwide</span><span class="label">Serving affected individuals and families across the United States</span></div>
        </div>
      </div>
    </section>

    <section>
      <div class="wrap center">
        <h2>What is a TRIP12-related disorder?</h2>
        <p class="section-intro">TRIP12-related disorder is a rare genetic condition caused by changes in the TRIP12 gene. It is often associated with developmental delay, intellectual disability, speech and language difficulties, and autism spectrum features. Because it is so rare, families frequently face long diagnostic journeys and significant out-of-pocket costs for the therapies and support their loved ones need. That's why we exist.</p>
        <a class="btn btn-primary" href="about.html">About the Foundation</a>
      </div>
    </section>

    <section class="band">
      <div class="wrap" style="padding-top:56px;padding-bottom:56px">
        <h2>Every gift goes further here</h2>
        <p>With an all-volunteer board and minimal overhead, your donation goes to families &mdash; not administration.</p>
        <a class="btn btn-amber" href="donate.html">Make a Tax-Deductible Gift</a>
      </div>
    </section>
"""

# ---------------- ABOUT ----------------
about = f"""
    <div class="page-head">
      <div class="wrap">
        <h1>About the Foundation</h1>
        <p>Founded by a family, built for families.</p>
      </div>
    </div>

    <section>
      <div class="wrap prose">
        <h2>Our mission</h2>
        <p>Trip 12 Future Foundation Inc. is organized to provide financial assistance, support services, and educational resources to individuals and families affected by the TRIP12 gene disorder and related neurodevelopmental conditions. Our work is designed to relieve financial hardship, advance health, and support families facing significant medical and developmental challenges associated with rare genetic disorders.</p>
        <p>We operate as a 501(c)(3) public charity and serve individuals throughout the United States.</p>

        <h2 style="margin-top:44px">Why "Trip 12"?</h2>
        <p>Our name comes from the TRIP12 gene. Changes in this gene cause a rare neurodevelopmental condition that affects children and families in profound ways &mdash; developmentally, medically, and financially. Families navigating a TRIP12 diagnosis often find few resources built specifically for them. We're working to change that.</p>
      </div>
    </section>

    <section class="alt">
      <div class="wrap">
        <h2 class="center" style="margin-bottom:36px">Board of Directors</h2>
        <div class="board-grid">
          <div class="card board-card">
            <div class="avatar" aria-hidden="true">SF</div>
            <h3>Steve Farrell</h3>
            <div class="role">President &amp; Treasurer</div>
            <p>Leads the Foundation's operations, programs, and finances.</p>
          </div>
          <div class="card board-card">
            <div class="avatar" aria-hidden="true">CF</div>
            <h3>Courtney Farrell</h3>
            <div class="role">Vice President &amp; Secretary</div>
            <p>Oversees governance, records, and family outreach.</p>
          </div>
          <div class="card board-card">
            <div class="avatar" aria-hidden="true">AQ</div>
            <h3>Andrea Quigley</h3>
            <div class="role">Independent Director</div>
            <p>Provides independent oversight and reviews any assistance request involving a founder's family.</p>
          </div>
        </div>
        <p class="center" style="margin-top:28px;color:var(--ink-soft)">All directors serve without compensation.</p>
      </div>
    </section>

    <section>
      <div class="wrap prose">
        <h2>Governance &amp; accountability</h2>
        <p>We hold ourselves to a high standard of transparency and stewardship:</p>
        <ul>
          <li><strong>Written Conflict of Interest and Recusal Policies.</strong> Any request for assistance involving a founder or family member is reviewed solely by our independent director, with founders recused from all discussion and decision-making.</li>
          <li><strong>Consistent criteria for everyone.</strong> The same eligibility criteria and documentation requirements apply to all applicants.</li>
          <li><strong>Direct-to-provider payments.</strong> Whenever possible, assistance is paid directly to medical providers, therapy clinics, and vendors rather than to individuals.</li>
          <li><strong>Complete records.</strong> We document every assistance award, including applications, approvals, and payments.</li>
          <li><strong>No private benefit.</strong> No part of the Foundation's net earnings benefits any private individual.</li>
        </ul>
        <div class="notice" style="margin-top:26px">
          <strong>Verify us:</strong> Trip 12 Future Foundation Inc. (EIN {EIN}) is listed in the IRS Tax Exempt Organization Search (Publication 78), confirming eligibility to receive tax-deductible charitable contributions.
        </div>
      </div>
    </section>
"""

# ---------------- PROGRAMS ----------------
programs = f"""
    <div class="page-head">
      <div class="wrap">
        <h1>Our Programs</h1>
        <p>Three ways we support individuals and families affected by TRIP12-related disorders and related neurodevelopmental conditions.</p>
      </div>
    </div>

    <section id="financial">
      <div class="wrap prose">
        <h2>1. Financial Assistance to Families</h2>
        <p>We provide direct financial assistance to qualifying families to help cover medically necessary expenses that are not fully covered by insurance or other assistance programs. Eligible expenses may include:</p>
        <ul>
          <li>Medical and specialist visits</li>
          <li>Occupational, physical, speech, or behavioral therapies</li>
          <li>Adaptive equipment and assistive technology</li>
          <li>Uncovered medical or therapeutic treatments</li>
          <li>Safety-related or developmental support items</li>
        </ul>
        <p>Whenever possible, assistance is paid directly to medical providers, therapy clinics, service organizations, or vendors. Where reimbursement is necessary, receipts and documentation are required.</p>
        <a class="btn btn-primary" href="apply.html">How to Apply</a>
      </div>
    </section>

    <section class="alt" id="service-animals">
      <div class="wrap prose">
        <h2>2. Service Animal Support</h2>
        <p>Service animals can be life-changing for individuals with neurological or developmental disabilities. We provide financial support related to the placement, training, and care of service animals that assist individuals affected by disabilities associated with genetic disorders.</p>
        <p>Eligible expenses may include training fees, placement costs, or related support services provided by qualified organizations. Applications for service animal support are reviewed using the same criteria and safeguards applied to all of our assistance programs.</p>
      </div>
    </section>

    <section id="education">
      <div class="wrap prose">
        <h2>3. Education, Awareness &amp; Community Support</h2>
        <p>We produce and distribute educational materials and conduct outreach to increase awareness of the TRIP12 gene disorder and the challenges affected families face. Our activities include:</p>
        <ul>
          <li>Educational content distributed online and in print</li>
          <li>Community awareness initiatives</li>
          <li>Small-scale informational and support events</li>
          <li>Resource sharing for families and caregivers</li>
        </ul>
        <p>All educational activities are offered free of charge.</p>
      </div>
    </section>

    <section class="band">
      <div class="wrap" style="padding-top:56px;padding-bottom:56px">
        <h2>Looking ahead</h2>
        <p>As resources grow, we plan to expand into broader outreach and support for research on genetic and neurodevelopmental disorders conducted by qualified nonprofit institutions.</p>
        <a class="btn btn-amber" href="donate.html">Help Us Grow</a>
      </div>
    </section>
"""

# ---------------- APPLY ----------------
apply = f"""
    <div class="page-head">
      <div class="wrap">
        <h1>Apply for Assistance</h1>
        <p>If your family is affected by a TRIP12-related disorder or a related neurodevelopmental condition, we may be able to help.</p>
      </div>
    </div>

    <section>
      <div class="wrap prose">
        <h2>Who is eligible</h2>
        <p>Financial assistance is available to individuals and families affected by the TRIP12 gene disorder or related neurodevelopmental conditions. Assistance is intended to relieve financial hardship related to medical, therapeutic, developmental, or safety needs. Applicants may live anywhere in the United States.</p>

        <h2 style="margin-top:44px">What can be covered</h2>
        <ul>
          <li>Medical and specialist visits</li>
          <li>Occupational, physical, speech, or behavioral therapies</li>
          <li>Adaptive equipment and assistive technology</li>
          <li>Service animal placement or training costs</li>
          <li>Uncovered medical or therapeutic treatments</li>
          <li>Safety-related or developmental support items</li>
        </ul>
      </div>
    </section>

    <section class="alt">
      <div class="wrap" style="max-width:820px">
        <h2>How to apply</h2>
        <p class="section-intro">Applications are reviewed by our Board of Directors on a case-by-case basis, using established eligibility criteria and available funding.</p>
        <ol class="steps">
          <li>
            <h3>Prepare your application</h3>
            <p>Write a brief application that includes your contact information, a description of the assistance you're requesting, and the amount or estimated cost involved.</p>
          </li>
          <li>
            <h3>Gather documentation</h3>
            <p>Include medical documentation confirming a qualifying diagnosis, documentation of financial need, and invoices, estimates, or receipts where applicable.</p>
          </li>
          <li>
            <h3>Submit your application online</h3>
            <p>Use the <a href="#application-form">application form below</a> &mdash; it takes about five minutes. We'll reply with instructions for sending your supporting documents securely.</p>
          </li>
          <li>
            <h3>Board review</h3>
            <p>Our board (or a designated review committee) reviews each application against established criteria. Approval requires a majority vote of disinterested directors.</p>
          </li>
          <li>
            <h3>Payment to your provider</h3>
            <p>If approved, we pay providers, clinics, or vendors directly whenever possible. Reimbursements are available in limited situations with receipts.</p>
          </li>
        </ol>
        <div class="notice" style="margin-top:26px">
          <strong>Fair for every family:</strong> Assistance decisions are made without regard to race, color, religion, sex, national origin, or any other protected classification. Any application involving a Foundation founder or family member is reviewed solely by our independent director.
        </div>
      </div>
    </section>

    <section id="application-form">
      <div class="wrap" style="max-width:760px">
        <h2>Start your application</h2>
        <p class="section-intro">This first step doesn't require any documents &mdash; just tell us who you are and what you need. Please don't include medical records or financial details here; we'll follow up with secure instructions for those.</p>
        {APPLICATION_FORM}
      </div>
    </section>
"""

# ---------------- DONATE ----------------
donate = f"""
    <div class="page-head">
      <div class="wrap">
        <h1>Donate</h1>
        <p>Your gift relieves real financial hardship for families facing rare genetic disorders.</p>
      </div>
    </div>

    <section>
      <div class="wrap" style="max-width:820px">
        <div class="card" style="text-align:center;padding:40px">
          <h2>Online giving is coming soon</h2>
          <p style="color:var(--ink-soft);max-width:520px;margin:0 auto 24px">We're finishing setup of our secure online donation processor. In the meantime, we'd love to hear from you directly &mdash; email us and we'll make giving easy.</p>
          <!-- TODO: Replace this button with the live donation link (e.g., Zeffy or PayPal) when ready -->
          <div class="btn-row">
            <a class="btn btn-amber" href="mailto:{EMAIL}?subject=I%20want%20to%20donate">Email Us to Give</a>
          </div>
        </div>

        <div style="margin-top:40px" class="prose">
          <h2>Where your money goes</h2>
          <p>Trip 12 Future Foundation is run by an all-volunteer board &mdash; no director or officer receives any compensation. Administrative costs are kept to a minimum, so contributions go to program services: direct assistance to families, service animal support, and free education for the community.</p>
          <h2 style="margin-top:36px">Tax-deductible giving</h2>
          <p>Trip 12 Future Foundation Inc. is a 501(c)(3) tax-exempt public charity (EIN {EIN}) listed in the IRS Tax Exempt Organization Search. Contributions are tax-deductible to the extent allowed by law. You will receive a written acknowledgment for your records.</p>
        </div>
      </div>
    </section>
"""

# ---------------- GET INVOLVED ----------------
involved = f"""
    <div class="page-head">
      <div class="wrap">
        <h1>Get Involved</h1>
        <p>There's more than one way to stand with TRIP12 families.</p>
      </div>
    </div>

    <section>
      <div class="wrap">
        <div class="card-grid">
          <div class="card">
            <h3>Volunteer</h3>
            <p>Help with awareness events, educational materials, fundraising, or outreach. Tell us a bit about yourself and how you'd like to help.</p>
            <a class="more" href="mailto:{EMAIL}?subject=Volunteering">Email us about volunteering &rarr;</a>
          </div>
          <div class="card">
            <h3>Spread the word</h3>
            <p>Most people have never heard of TRIP12-related disorders. Sharing our mission with your friends, workplace, or community helps families find us &mdash; and helps us find them.</p>
            <a class="more" href="about.html">Learn our story &rarr;</a>
          </div>
          <div class="card">
            <h3>Workplace &amp; matching gifts</h3>
            <p>Many employers match charitable donations or sponsor community causes. Ask your HR team whether they'll match your gift to Trip 12 Future Foundation (EIN {EIN}).</p>
            <a class="more" href="donate.html">Go to donations &rarr;</a>
          </div>
          <div class="card">
            <h3>Share your family's story</h3>
            <p>If your family has been touched by a TRIP12 diagnosis, your story can encourage others and raise awareness. We only share stories with your written permission.</p>
            <a class="more" href="mailto:{EMAIL}?subject=Our%20story">Reach out &rarr;</a>
          </div>
        </div>
      </div>
    </section>

    <section class="alt">
      <div class="wrap" style="max-width:760px">
        <h2>Volunteer sign-up</h2>
        <p class="section-intro">Tell us a bit about yourself and how you'd like to help &mdash; we'll reach out.</p>
        {VOLUNTEER_FORM}
      </div>
    </section>

    <section class="band">
      <div class="wrap" style="padding-top:56px;padding-bottom:56px">
        <h2>Have another idea?</h2>
        <p>Fundraisers, events, partnerships &mdash; we're a small foundation and we welcome creative help.</p>
        <a class="btn btn-amber" href="contact.html">Contact Us</a>
      </div>
    </section>
"""

# ---------------- NEWS ----------------
news = f"""
    <div class="page-head">
      <div class="wrap">
        <h1>News &amp; Events</h1>
        <p>Milestones, updates, and upcoming events from the Foundation.</p>
      </div>
    </div>

    <section>
      <div class="wrap" style="max-width:760px">
        <article class="news-item">
          <time datetime="2026-08">August 2026</time>
          <h3>Our website is live</h3>
          <p>Welcome! This site is the new home for everything Trip 12 Future Foundation &mdash; how to apply for assistance, how to give, and how to get involved. Online donations are coming soon.</p>
        </article>
        <article class="news-item">
          <time datetime="2026">2026</time>
          <h3>IRS recognizes Trip 12 Future Foundation as a 501(c)(3) public charity</h3>
          <p>The Foundation is officially listed in the IRS Tax Exempt Organization Search (Publication 78), which means contributions are tax-deductible. This milestone lets us grow our assistance programs with confidence.</p>
        </article>
        <article class="news-item">
          <time datetime="2025-11">November 2025</time>
          <h3>Foundation incorporated and first families assisted</h3>
          <p>Trip 12 Future Foundation Inc. was incorporated in Utah, held its first board meeting, and began charitable operations by providing initial financial assistance consistent with our mission.</p>
        </article>
        <div class="notice">
          <strong>Upcoming events:</strong> None scheduled just yet &mdash; check back soon, or <a href="get-involved.html">get involved</a> and help us plan our first community event.
        </div>
      </div>
    </section>
"""

# ---------------- GALLERY ----------------
gallery = f"""
    <div class="page-head">
      <div class="wrap">
        <h1>Gallery</h1>
        <p>Faces, moments, and milestones from the Trip 12 community.</p>
      </div>
    </div>

    <section>
      <div class="wrap">
        <p class="section-intro">We're just getting started &mdash; photos from our first events and family stories will appear here soon.</p>
        <div class="gallery-grid">
          <div class="gallery-ph">Photo coming soon</div>
          <div class="gallery-ph">Photo coming soon</div>
          <div class="gallery-ph">Photo coming soon</div>
          <div class="gallery-ph">Photo coming soon</div>
          <div class="gallery-ph">Photo coming soon</div>
          <div class="gallery-ph">Photo coming soon</div>
        </div>
        <p style="margin-top:28px;color:var(--ink-soft)">Have photos from a Foundation event or a story to share? We'd love to feature them (with your permission) &mdash; <a href="mailto:{EMAIL}?subject=Gallery%20photos">send them our way</a>.</p>
      </div>
    </section>
"""

# ---------------- CONTACT ----------------
contact = f"""
    <div class="page-head">
      <div class="wrap">
        <h1>Contact Us</h1>
        <p>We're a small, family-run foundation &mdash; you'll hear back from a real person.</p>
      </div>
    </div>

    <section>
      <div class="wrap" style="max-width:760px">
        <dl class="def-list">
          <div>
            <dt>Email</dt>
            <dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
          </div>
          <div>
            <dt>Assistance applications</dt>
            <dd>Email with subject line &ldquo;Assistance Application&rdquo; &mdash; see <a href="apply.html">how to apply</a>.</dd>
          </div>
          <div>
            <dt>Donations</dt>
            <dd>See our <a href="donate.html">donate page</a>, or email with subject &ldquo;Donation.&rdquo;</dd>
          </div>
          <div>
            <dt>Location</dt>
            <dd>Clinton, Utah &mdash; serving families across the United States</dd>
          </div>
          <div>
            <dt>Legal name &amp; EIN</dt>
            <dd>Trip 12 Future Foundation Inc. &middot; EIN {EIN} &middot; 501(c)(3) public charity</dd>
          </div>
        </dl>
      </div>
    </section>

    <section class="alt">
      <div class="wrap" style="max-width:760px">
        <h2>Send us a message</h2>
        <p class="section-intro">The fastest way to reach us &mdash; your message goes straight to the board.</p>
        {CONTACT_FORM}
      </div>
    </section>
"""

# ---------------- THANKS ----------------
thanks = f"""
    <div class="hero">
      <div class="wrap" style="padding-top:80px;padding-bottom:72px">
        <span class="eyebrow">Message received</span>
        <h1>Thank you!</h1>
        <p class="lede">We got your submission and a real person &mdash; one of our board members &mdash; will get back to you as soon as we can, usually within a few days.</p>
        <div class="btn-row">
          <a class="btn btn-amber" href="index.html">Back to Home</a>
          <a class="btn btn-secondary" href="programs.html">Explore Our Programs</a>
        </div>
      </div>
    </div>
"""

pages = [
    ("index.html", "Trip 12 Future Foundation | Hope for TRIP12 Families",
     "Trip 12 Future Foundation is a 501(c)(3) charity providing financial assistance, service animal support, and education for families affected by TRIP12-related disorders.", home),
    ("about.html", "About | Trip 12 Future Foundation",
     "Our mission, board of directors, and governance. A family-founded 501(c)(3) serving families affected by TRIP12-related disorders.", about),
    ("programs.html", "Programs | Trip 12 Future Foundation",
     "Financial assistance to families, service animal support, and free education and awareness programs for TRIP12-related disorders.", programs),
    ("apply.html", "Apply for Assistance | Trip 12 Future Foundation",
     "How to apply for financial assistance for medical, therapeutic, developmental, or safety needs related to TRIP12 and related neurodevelopmental conditions.", apply),
    ("donate.html", "Donate | Trip 12 Future Foundation",
     "Make a tax-deductible gift to Trip 12 Future Foundation, a 501(c)(3) public charity supporting families affected by TRIP12-related disorders.", donate),
    ("get-involved.html", "Get Involved | Trip 12 Future Foundation",
     "Volunteer, spread awareness, set up workplace matching, or share your story with Trip 12 Future Foundation.", involved),
    ("news.html", "News & Events | Trip 12 Future Foundation",
     "Milestones, updates, and upcoming events from Trip 12 Future Foundation.", news),
    ("gallery.html", "Gallery | Trip 12 Future Foundation",
     "Photos and moments from the Trip 12 Future Foundation community.", gallery),
    ("contact.html", "Contact | Trip 12 Future Foundation",
     "Contact Trip 12 Future Foundation — send a message, apply for assistance, or ask about donations.", contact),
    ("thanks.html", "Thank You | Trip 12 Future Foundation",
     "Thanks — we received your submission and will be in touch soon.", thanks),
]

# favicon
with open(os.path.join(OUT, "img", "favicon.svg"), "w") as f:
    f.write(LOGO)

for fn, title, desc, body in pages:
    page(fn, title, desc, body)

print("done")
