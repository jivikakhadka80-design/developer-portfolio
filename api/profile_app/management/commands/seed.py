from django.core.management.base import BaseCommand
from profile_app.models import (Profile, AboutCard, Experience, BusinessModule,
                                FrameworkTopic, ToolGroup)


def fill(model, rows):
    model.objects.all().delete()
    model.objects.bulk_create([model(order=i, **r) for i, r in enumerate(rows, 1)])


class Command(BaseCommand):

    def handle(self, *args, **opts):
        Profile.objects.all().delete()
        Profile.objects.create(
            name="Rita Khadka", also_known_as="Jivika Khadka",
            role="Python Backend Developer (Odoo ERP)",
            availability="Open to mid-level developer roles",
            intro="I build practical, reliable Odoo solutions by turning business requirements into clean, maintainable code.",
            chips="2.5 years in Odoo",
            email="jivikakhadka80@gmail.com", phone="+977 9844124517",
            gitlab="https://gitlab.com/Jivika-K",
            linkedin="https://www.linkedin.com/in/jivika-khadka-2104972a8/",
            degree="BSc CSIT", institution="Bhaktapur Multiple Campus · passed 2025")

        fill(AboutCard, [
            dict(title="How I work", text="Before writing code, I first understand the existing workflow and identify where improvements are needed. Then I build practical Odoo solutions using standard features whenever possible and custom development when necessary. I follow Odoo best practices, avoid modifying core code, and test everything before deployment."),
            dict(title="Backend focus", text="I focus on Python, the Odoo ORM, and PostgreSQL to build efficient and reliable backend solutions. I pay attention to code quality, database performance, and optimizing business logic to keep Odoo applications running smoothly."),
            dict(title="Business side", text="HRMS, sales, accounting, purchase and inventory, where one wrong number in one place shows up everywhere else. Tax reports must match the books, so I check real cases, not only the easy ones."),
        ])

        fill(Experience, [
            dict(
                role="Odoo / Python Backend Developer",
                company="Nexus Incorporation Pvt. Ltd. · kalanki, Kathmandu, Nepal",
                period="May 2026 - Present",
                description="Develop and maintain custom Odoo modules across versions 12 to 20, covering Accounting, Sales, Purchase, Inventory and Manufacturing. Build REST APIs in Odoo 19 for external system integration, including Bearer token authentication, product and customer synchronization, order and payment management, ticket generation, QR-based check-in and status synchronization. Work on payment gateway integration through Odoo APIs, IRD reports and business workflow customisations. Handle backend development, debugging, production issues and GitLab-based code reviews.",
                tags="Odoo 12–20, Python, REST API, API Integration, Payment Gateway, Accounting, Sales, Purchase, Inventory"
            ),
            dict(
                role="Odoo Developer",
                company="ING Group · Kamal Marg, Kathmandu, Nepal",
                period="Aug 2024 - Apr 2026",
                description="Designed and developed a complete multi-company HRMS in Odoo, covering Employee Management, Attendance, Leave Management, Payroll, Expenses and Recruitment. Implemented company-specific HR policies, payroll calculations, tax rules, employee workflows and automated processes. Worked with business requirements and translated HR and financial processes into customised ERP solutions. Gained practical understanding of Accounting, Sales, Purchase and procurement workflows through cross-functional ERP operations.",
                tags="Multi-Company, HRMS, Payroll, Attendance, Leave, Python, XML"
            ),
            dict(
                role="Odoo Developer Intern",
                company="Shreem IT  · Suryabinayak, Bhaktapur, Nepal",
                period="Mar 2024 - Jun 2024",
                description="Worked with the development team on Odoo ERP customisation and e-commerce application development. Gained hands-on experience in Odoo module development, Python, XML, ORM, model creation, views and business workflows. Assisted in developing and customising backend features while learning ERP business processes.",
                tags="Odoo, Python, XML, ORM, Django, Backend Development"
            ),
        ])


        fill(BusinessModule, [
            dict(name="Accounting"),
            dict(name="Inventory"),
            dict(name="Sales & CRM"),
            dict(name="Purchase"),
            dict(name="HR & Payroll"),
            dict(name="Manufacturing (MRP)"),
            dict(name="Projects"),
        ])

        fill(FrameworkTopic, [
            dict(title="Custom module development", description="Developing custom Odoo modules and extending standard functionality to meet business requirements."),
            dict(title="ORM and inheritance", description="Extending models using _inherit, computed and stored fields, relational fields, constraints and business logic."),
            dict(title="Security and multi-company", description="Configuring access control lists, security groups, record rules and multi-company access."),
            dict(title="XML views and workflows", description="Building form, list and search views, view inheritance, XPath modifications, buttons and automated workflows."),
            dict(title="Reports", description="Developing QWeb PDF and Excel reports, including business and IRD tax reporting formats."),
            dict(title="OWL development", description="Building interactive Odoo frontend components using OWL and JavaScript."),
            dict(title="REST API development", description="Creating custom Odoo REST APIs with Bearer-token authentication, JSON responses, validation, error handling and external system synchronization."),
            dict(title="Third-party integrations", description="Integrating payment gateways and external APIs to connect Odoo with third-party applications and services."),
            dict(title="GitLab and server management", description="Managing source code with GitLab, pulling code updates, installing external Python libraries and handling server-side dependencies."),
            dict(title="Odoo versions",description="Experience developing, customising and maintaining Odoo solutions across versions 12 to 20."),
        ])

        fill(ToolGroup, [
            dict(title="Backend",items="Python, Django, Django REST Framework (DRF), REST APIs, XML-RPC / JSON-RPC, Scheduled jobs"),
            dict(title="Odoo", items="ORM & inheritance, Custom modules, QWeb reports, ACL & record rules, Version migrations"),
            dict(title="Database",items="PostgreSQL, Odoo ORM, Query tuning, Indexing strategy, Bulk data migration, Backup & recovery"),
            dict(title="Frontend",items="JavaScript, XML views, QWeb templates, SCSS, HTML and CSS"),
            dict(title="Tools",items="Git, GitLab, VS Code / PyCharm, pgAdmin, & Postman"),
        ])
        self.stdout.write(self.style.SUCCESS("Seeded."))
