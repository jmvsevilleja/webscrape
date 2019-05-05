import requests
from bs4 import BeautifulSoup
from csv import writer

text = """
<div class="wsp-container"><h2 class="wsp-pages-title">Pages</h2>
<ul class="wsp-pages-list">
<li class="page_item page-item-1833"><a href="https://www.intellichoice.com.au/1-year-fixed-home-loans">1 Year Fixed Home Loan</a></li>
<li class="page_item page-item-2298"><a href="https://www.intellichoice.com.au/10-year-fixed-rate-home-loan">10 Year Fixed Rate Home Loan</a></li>
<li class="page_item page-item-1856"><a href="https://www.intellichoice.com.au/15-year-fixed-rate-home-loan">15 Year Fixed Rate Home Loan</a></li>
<li class="page_item page-item-1841"><a href="https://www.intellichoice.com.au/3-year-fixed-rate-home-loan">3 Year Fixed Rate Home Loan</a></li>
<li class="page_item page-item-1850"><a href="https://www.intellichoice.com.au/5-year-fixed-rate-home-loan">5 Year Fixed Rate Home Loan</a></li>
<li class="page_item page-item-1870"><a href="https://www.intellichoice.com.au/90-home-loan">90% Home Loan</a></li>
<li class="page_item page-item-1863"><a href="https://www.intellichoice.com.au/95-home-loan">95% Home Loan</a></li>
<li class="page_item page-item-1247"><a href="https://www.intellichoice.com.au/about">About Us</a></li>
<li class="page_item page-item-2338"><a href="https://www.intellichoice.com.au/articles-bad-credit-car-loans">Articles Bad Credit Car Loans</a></li>
<li class="page_item page-item-1759"><a href="https://www.intellichoice.com.au/asset-finance">Asset Finance</a></li>
<li class="page_item page-item-2545"><a href="https://www.intellichoice.com.au/asset-finance-articles-videos">Asset Finance Articles and Videos</a></li>
<li class="page_item page-item-3248"><a href="https://www.intellichoice.com.au/asset-finance-videos">Asset Finance Videos</a></li>
<li class="page_item page-item-2330"><a href="https://www.intellichoice.com.au/bad-credit-car-finance-process">Bad Credit Car Finance Process</a></li>
<li class="page_item page-item-5276"><a href="https://www.intellichoice.com.au/bad-credit-car-loan-videos">Bad Credit Car Loan Videos</a></li>
<li class="page_item page-item-1730"><a href="https://www.intellichoice.com.au/bad-credit-car-loans">Bad Credit Car Loans</a></li>
<li class="page_item page-item-1773"><a href="https://www.intellichoice.com.au/bad-credit-equipment-finance">Bad Credit Equipment Finance</a></li>
<li class="page_item page-item-2296"><a href="https://www.intellichoice.com.au/bad-credit-home-loan-articles">Bad Credit Home Loan Articles</a></li>
<li class="page_item page-item-1622"><a href="https://www.intellichoice.com.au/bad-credit-home-loans">Bad Credit Home Loans</a></li>
<li class="page_item page-item-8581"><a href="https://www.intellichoice.com.au/bad-credit-home-loans-2">Bad Credit Home Loans</a></li>
<li class="page_item page-item-8588"><a href="https://www.intellichoice.com.au/bad-credit-home-loans-3">Bad Credit Home Loans</a></li>
<li class="page_item page-item-8579"><a href="https://www.intellichoice.com.au/bad-credit-home-loans-australia">Bad Credit Home Loans Australia</a></li>
<li class="page_item page-item-8590"><a href="https://www.intellichoice.com.au/bad-credit-home-loans-australia-2">Bad Credit Home Loans Australia</a></li>
<li class="page_item page-item-3189"><a href="https://www.intellichoice.com.au/bad-credit-home-loans-videos">Bad Credit Home Loans Videos</a></li>
<li class="page_item page-item-8584"><a href="https://www.intellichoice.com.au/bad-credit-loans-australia-guaranteed-approval">Bad Credit Loans Australia Guaranteed Approval</a></li>
<li class="page_item page-item-8592"><a href="https://www.intellichoice.com.au/bad-credit-loans-australia-guaranteed-approval-2">Bad Credit Loans Australia Guaranteed Approval</a></li>
<li class="page_item page-item-1796"><a href="https://www.intellichoice.com.au/basic-variable-home-loan">Basic Variable Home Loan</a></li>
<li class="page_item page-item-2249"><a href="https://www.intellichoice.com.au/borrowing-power">Borrowing Power Calculator</a></li>
<li class="page_item page-item-4688"><a href="https://www.intellichoice.com.au/broker-specialist-articles">Broker Specialist Articles</a></li>
<li class="page_item page-item-2252"><a href="https://www.intellichoice.com.au/budget-planner">Budget Planner Calculator</a></li>
<li class="page_item page-item-4301"><a href="https://www.intellichoice.com.au/business-finance-articles">Business Finance Articles by Intellichoice Finance</a></li>
<li class="page_item page-item-2361"><a href="https://www.intellichoice.com.au/business-finance">Business Finance Australia</a></li>
<li class="page_item page-item-4298"><a href="https://www.intellichoice.com.au/business-finance-videos">Business Finance Videos by Intellichoice Finance</a></li>
<li class="page_item page-item-8594"><a href="https://www.intellichoice.com.au/business-loans">Business Loans</a></li>
<li class="page_item page-item-8597"><a href="https://www.intellichoice.com.au/car-loan">Car Loan</a></li>
<li class="page_item page-item-3183"><a href="https://www.intellichoice.com.au/car-loan-videos">Car Loan Videos</a></li>
<li class="page_item page-item-1503"><a href="https://www.intellichoice.com.au/car-loans">Car Loans</a></li>
<li class="page_item page-item-1781"><a href="https://www.intellichoice.com.au/commercial-funding">Commercial Funding</a></li>
<li class="page_item page-item-2375"><a href="https://www.intellichoice.com.au/commercial-loans">Commercial Loans</a></li>
<li class="page_item page-item-3413"><a href="https://www.intellichoice.com.au/comparison-rate-calculator">Comparison Rate Calculator</a></li>
<li class="page_item page-item-3450"><a href="https://www.intellichoice.com.au/compound-interest-calculator">Compound Interest Calculator</a></li>
<li class="page_item page-item-5307"><a href="https://www.intellichoice.com.au/construction-loans">Construction Loans</a></li>
<li class="page_item page-item-5401"><a href="https://www.intellichoice.com.au/construction-loans-articles">Construction Loans Articles by Intellichoice Finance</a></li>
<li class="page_item page-item-8599"><a href="https://www.intellichoice.com.au/construction-loans-australia">Construction Loans Australia</a></li>
<li class="page_item page-item-5310"><a href="https://www.intellichoice.com.au/construction-loans-videos">Construction Loans Videos by Intellichoice Finance</a></li>
<li class="page_item page-item-1281"><a href="https://www.intellichoice.com.au/contact">Contact</a></li>
<li class="page_item page-item-2254"><a href="https://www.intellichoice.com.au/credit-card">Credit Card Calculator</a></li>
<li class="page_item page-item-1891"><a href="https://www.intellichoice.com.au/development-finance">Development Finance by Intellichoice Finance</a></li>
<li class="page_item page-item-2383"><a href="https://www.intellichoice.com.au/equipment-finance-articles">Equipment Finance Articles</a></li>
<li class="page_item page-item-3258"><a href="https://www.intellichoice.com.au/equipment-finance-videos">Equipment Finance Videos</a></li>
<li class="page_item page-item-8603"><a href="https://www.intellichoice.com.au/equipment-loans">Equipment Loans</a></li>
<li class="page_item page-item-2388"><a href="https://www.intellichoice.com.au/expat-foreign-owner-education">Expat Foreign Owner Education</a></li>
<li class="page_item page-item-1701"><a href="https://www.intellichoice.com.au/expat-foreign-owner-loans">Expat Foreign Owner Loans</a></li>
<li class="page_item page-item-3201"><a href="https://www.intellichoice.com.au/expat-foreign-owner-loans-videos">Expat Foreign Owner Loans Videos</a></li>
<li class="page_item page-item-2256"><a href="https://www.intellichoice.com.au/extra-repayments">Extra Repayments Calculator</a></li>
<li class="page_item page-item-16"><a href="https://www.intellichoice.com.au/">Finance For Lifestyle</a></li>
<li class="page_item page-item-2393"><a href="https://www.intellichoice.com.au/find-loan-expat-foreign-owner-loans">Find a Loan Expat Foreign Owner Loans</a></li>
<li class="page_item page-item-2561"><a href="https://www.intellichoice.com.au/fixed-home-loan">Fixed Home Loan</a></li>
<li class="page_item page-item-3309"><a href="https://www.intellichoice.com.au/fixed-home-loan-articles">Fixed Home Loan Articles by Intellichoice Finance</a></li>
<li class="page_item page-item-3314"><a href="https://www.intellichoice.com.au/fixed-home-loan-videos">Fixed Home Loan Videos by Intellichoice Finance</a></li>
<li class="page_item page-item-3473"><a href="https://www.intellichoice.com.au/fortnightly-repayment-calculator">Fortnightly Repayment Calculator</a></li>
<li class="page_item page-item-1902"><a href="https://www.intellichoice.com.au/franchise-funding">Franchise Funding</a></li>
<li class="page_item page-item-1914"><a href="https://www.intellichoice.com.au/home-loan-application-form">Home Loan Application Form</a></li>
<li class="page_item page-item-2259"><a href="https://www.intellichoice.com.au/home-loan-offset">Home Loan Offset Calculator</a></li>
<li class="page_item page-item-8612"><a href="https://www.intellichoice.com.au/home-loans-2">Home Loans</a></li>
<li class="page_item page-item-3508"><a href="https://www.intellichoice.com.au/home-loans">Home Loans</a></li>
<li class="page_item page-item-4679"><a href="https://www.intellichoice.com.au/home-loans-articles-resources">Home Loans Articles and Resources</a></li>
<li class="page_item page-item-2264"><a href="https://www.intellichoice.com.au/how-long-to-repay">How Long to Repay Calculator</a></li>
<li class="page_item page-item-3460"><a href="https://www.intellichoice.com.au/income-annualisation-calculator">Income Annualisation Calculator</a></li>
<li class="page_item page-item-3463"><a href="https://www.intellichoice.com.au/income-gross-up-calculator">Income Gross Up Calculator</a></li>
<li class="page_item page-item-2267"><a href="https://www.intellichoice.com.au/income-tax">Income Tax Calculator</a></li>
<li class="page_item page-item-4691"><a href="https://www.intellichoice.com.au/industry-experience-articles-resources">Industry Experience Articles &amp; Resources</a></li>
<li class="page_item page-item-1605"><a href="https://www.intellichoice.com.au/insurance">Insurance</a></li>
<li class="page_item page-item-3330"><a href="https://www.intellichoice.com.au/insurance-articles">Insurance Articles</a></li>
<li class="page_item page-item-3333"><a href="https://www.intellichoice.com.au/insurance-videos">Insurance Videos</a></li>
<li class="page_item page-item-2366"><a href="https://www.intellichoice.com.au/intellichoice-calculators">Intellichoice Calculators</a></li>
<li class="page_item page-item-2305"><a href="https://www.intellichoice.com.au/intellichoice-expat-foreign-owner-loan-articles-videos">Intellichoice Expat Foreign Owner Loan Articles</a></li>
<li class="page_item page-item-9425"><a href="https://www.intellichoice.com.au/intellichoice-expat-mortgages-buy-before-you-come-home">Intellichoice Expat Mortgages – Buy Before you come Home</a></li>
<li class="page_item page-item-3403"><a href="https://www.intellichoice.com.au/interest-only-mortgage-calculator">Interest Only Mortgage Calculator</a></li>
<li class="page_item page-item-1822"><a href="https://www.intellichoice.com.au/introductory-home-loan">Introductory Home Loan</a></li>
<li class="page_item page-item-3436"><a href="https://www.intellichoice.com.au/introductory-rate-loan-calculator">Introductory Rate Loan Calculator</a></li>
<li class="page_item page-item-1908"><a href="https://www.intellichoice.com.au/inventory-finance">Inventory Finance</a></li>
<li class="page_item page-item-3219"><a href="https://www.intellichoice.com.au/inventory-finance-articles">Inventory Finance Articles by Intellichoice Finance</a></li>
<li class="page_item page-item-3223"><a href="https://www.intellichoice.com.au/inventory-finance-videos">Inventory Finance Videos</a></li>
<li class="page_item page-item-1610"><a href="https://www.intellichoice.com.au/investment-and-advice">Investment and Advice</a></li>
<li class="page_item page-item-3226"><a href="https://www.intellichoice.com.au/investment-and-advice-articles">Investment and Advice Articles by Intellichoice Finance</a></li>
<li class="page_item page-item-3232"><a href="https://www.intellichoice.com.au/investment-and-advice-videos">Investment and Advice Videos by Intellichoice Finance</a></li>
<li class="page_item page-item-8614"><a href="https://www.intellichoice.com.au/invoice-finance-2">Invoice Finance</a></li>
<li class="page_item page-item-1738"><a href="https://www.intellichoice.com.au/invoice-finance">Invoice Finance</a></li>
<li class="page_item page-item-2323"><a href="https://www.intellichoice.com.au/invoice-finance-articles">Invoice Finance Articles by Intellichoice Finance</a></li>
<li class="page_item page-item-3239"><a href="https://www.intellichoice.com.au/invoice-finance-videos">Invoice Finance Videos</a></li>
<li class="page_item page-item-2269"><a href="https://www.intellichoice.com.au/leasing">Leasing Calculator</a></li>
<li class="page_item page-item-4448"><a href="https://www.intellichoice.com.au/lifestyle-loans">Lifestyle Loans</a></li>
<li class="page_item page-item-4674"><a href="https://www.intellichoice.com.au/loan-calculators-articles">Loan Calculators Articles</a></li>
<li class="page_item page-item-2272"><a href="https://www.intellichoice.com.au/loan-comparison">Loan Comparison Calculator</a></li>
<li class="page_item page-item-2275"><a href="https://www.intellichoice.com.au/loan-repayment">Loan Repayment Calculator</a></li>
<li class="page_item page-item-5291"><a href="https://www.intellichoice.com.au/low-doc-construction-loans">Low Doc Construction Loans</a></li>
<li class="page_item page-item-5300"><a href="https://www.intellichoice.com.au/low-doc-construction-loans-articles">Low Doc Construction Loans Articles | Intellichoice Finance</a></li>
<li class="page_item page-item-5294"><a href="https://www.intellichoice.com.au/low-doc-construction-loans-videos">Low Doc Construction Loans Videos | Intellichoice Finance</a></li>
<li class="page_item page-item-2277"><a href="https://www.intellichoice.com.au/lump-sum">Lump Sum Repayment Calculator</a></li>
<li class="page_item page-item-3475"><a href="https://www.intellichoice.com.au/mortgage-switching-calculator">Mortgage Switching Calculator</a></li>
<li class="page_item page-item-1717"><a href="https://www.intellichoice.com.au/other-home-loans">Other Home Loans</a></li>
<li class="page_item page-item-2308"><a href="https://www.intellichoice.com.au/owner-builder-home-loan-articles">Owner Builder Home Loan Articles</a></li>
<li class="page_item page-item-3109"><a href="https://www.intellichoice.com.au/owner-builder-home-loan-videos">Owner Builder Home Loan Videos</a></li>
<li class="page_item page-item-1643"><a href="https://www.intellichoice.com.au/owner-builder-home-loans">Owner Builder Home Loans</a></li>
<li class="page_item page-item-2515"><a href="https://www.intellichoice.com.au/owner-builder-lawyer-tap">Owner Builder Lawyer on Tap</a></li>
<li class="page_item page-item-8616"><a href="https://www.intellichoice.com.au/owner-builder-loans">Owner Builder Loans</a></li>
<li class="page_item page-item-8620"><a href="https://www.intellichoice.com.au/owner-builder-loans-australia">Owner Builder Loans Australia</a></li>
<li class="page_item page-item-2503"><a href="https://www.intellichoice.com.au/owner-builder-online-course">Owner Builder Online Course</a></li>
<li class="page_item page-item-7353"><a href="https://www.intellichoice.com.au/personal">Personal Loans</a></li>
<li class="page_item page-item-1499"><a href="https://www.intellichoice.com.au/personal-loans">Personal Loans</a></li>
<li class="page_item page-item-4787"><a href="https://www.intellichoice.com.au/personal-loans-articles">Personal Loans Articles</a></li>
<li class="page_item page-item-2280"><a href="https://www.intellichoice.com.au/property-buying-cost">Property Buying Cost Calculator</a></li>
<li class="page_item page-item-2282"><a href="https://www.intellichoice.com.au/property-selling-cost">Property Selling Cost Calculator</a></li>
<li class="page_item page-item-5443"><a href="https://www.intellichoice.com.au/quick-application-form-for-bad-credit-home-loans">Quick Application Form for Bad Credit Home Loans</a></li>
<li class="page_item page-item-3479"><a href="https://www.intellichoice.com.au/rent-vs-buy-calculator">Rent vs Buy Calculator</a></li>
<li class="page_item page-item-2284"><a href="https://www.intellichoice.com.au/reverse-mortgage">Reverse Mortgage Calculator</a></li>
<li class="page_item page-item-2287"><a href="https://www.intellichoice.com.au/savings">Savings Calculator</a></li>
<li class="page_item page-item-3467"><a href="https://www.intellichoice.com.au/savings-goal-calculator-how-long-to-save-how-long-to-save">Savings Goal Calculator How Long to Save</a></li>
<li class="page_item page-item-3470"><a href="https://www.intellichoice.com.au/savings-goal-calculator-how-much-to-deposit">Savings Goal Calculator How Much to Deposit</a></li>
<li class="page_item page-item-1689"><a href="https://www.intellichoice.com.au/self-managed-super-fund-loans">Self Managed Super Fund Loans</a></li>
<li class="page_item page-item-3195"><a href="https://www.intellichoice.com.au/self-managed-super-fund-loans-videos">Self Managed Super Fund Loans Videos</a></li>
<li class="page_item page-item-2325"><a href="https://www.intellichoice.com.au/self-managed-super-funds-articles">Self Managed Super Funds Articles</a></li>
<li class="page_item page-item-1884"><a href="https://www.intellichoice.com.au/short-term-finance">Short Term Finance</a></li>
<li class="page_item page-item-8574 current_page_item"><a href="https://www.intellichoice.com.au/sitemap" aria-current="page">Sitemap – Intellichoice Finance</a></li>
<li class="page_item page-item-2289"><a href="https://www.intellichoice.com.au/split-loan">Split Loan Calculator</a></li>
<li class="page_item page-item-2291"><a href="https://www.intellichoice.com.au/stamp-duty">Stamp Duty Calculator</a></li>
<li class="page_item page-item-1805"><a href="https://www.intellichoice.com.au/standard-variable-home-loan">Standard Variable Home Loan</a></li>
<li class="page_item page-item-2294"><a href="https://www.intellichoice.com.au/term-deposit">Term Deposit</a></li>
<li class="page_item page-item-2528"><a href="https://www.intellichoice.com.au/testimonials">Testimonials</a></li>
<li class="page_item page-item-4363"><a href="https://www.intellichoice.com.au/tos-and-privacy-policy">TOS and Privacy Policy</a></li>
<li class="page_item page-item-8624"><a href="https://www.intellichoice.com.au/trade-finance-2">Trade Finance</a></li>
<li class="page_item page-item-1749"><a href="https://www.intellichoice.com.au/trade-finance">Trade Finance</a></li>
<li class="page_item page-item-2319"><a href="https://www.intellichoice.com.au/trade-finance-articles">Trade Finance Articles</a></li>
<li class="page_item page-item-3346"><a href="https://www.intellichoice.com.au/trade-finance-videos">Trade Finance Videos</a></li>
<li class="page_item page-item-9433"><a href="https://www.intellichoice.com.au/video-intellichoice-integrated-business-finance">Video – Intellichoice – Integrated Business Finance</a></li>
<li class="page_item page-item-9431"><a href="https://www.intellichoice.com.au/video-intellichoice-short-term-finance">Video – Intellichoice – Short Term Finance</a></li>
<li class="page_item page-item-9429"><a href="https://www.intellichoice.com.au/video-intellichoice-trade-finance">Video – Intellichoice – Trade Finance</a></li>
<li class="page_item page-item-9435"><a href="https://www.intellichoice.com.au/video-intellichoice-equipment-finance">Video – Intellichoice Equipment Finance</a></li>
<li class="page_item page-item-9452"><a href="https://www.intellichoice.com.au/video-intellichoice-how-is-the-current-environment-impacting-borrowers">Video – Intellichoice How Is The Current Environment Impacting Borrowers</a></li>
<li class="page_item page-item-9421"><a href="https://www.intellichoice.com.au/intellichoice-is-on-the-side-of-the-client">Video – Intellichoice Is On The Side Of The Client</a></li>
<li class="page_item page-item-9437"><a href="https://www.intellichoice.com.au/video-intellichoice-niche-business-finance-products">Video – Intellichoice Niche Business Finance Products</a></li>
<li class="page_item page-item-9412"><a href="https://www.intellichoice.com.au/video-owner-builder-loan-specialists">Video – Owner Builder Loan Specialists</a></li>
<li class="page_item page-item-9443"><a href="https://www.intellichoice.com.au/video-susan-explains-how-to-make-owner-builder-loans-easier">Video – Susan Explains How To Make Owner Builder Loans Easier</a></li>
<li class="page_item page-item-9458"><a href="https://www.intellichoice.com.au/video-what-farmers-need-to-know-about-insurance">Video – What Farmers Need To Know About Insurance</a></li>
<li class="page_item page-item-9450"><a href="https://www.intellichoice.com.au/video-why-go-with-intellichoice-for-your-owner-builder-loan">Video – Why Go With Intellichoice For Your Owner Builder Loan</a></li>
<li class="page_item page-item-9456"><a href="https://www.intellichoice.com.au/video-why-is-an-owner-builder-home-loan-different">Video – Why Is An Owner Builder Home Loan Different</a></li>
<li class="page_item page-item-9454"><a href="https://www.intellichoice.com.au/video-why-is-an-owner-builder-loan-different-from-a-standard-home-loan">Video – Why Is An Owner Builder Loan Different From A Standard Home Loan</a></li>
<li class="page_item page-item-9448"><a href="https://www.intellichoice.com.au/video-why-owner-builder-loans-are-different-michelle-and-susan">Video – Why Owner Builder Loans Are Different – Michelle and Susan</a></li>
<li class="page_item page-item-9427"><a href="https://www.intellichoice.com.au/video-why-people-choose-intellichoice-financial-services">Video – Why People Choose Intellichoice Financial Services</a></li>
<li class="page_item page-item-9405"><a href="https://www.intellichoice.com.au/video-why-we-specialize-in-owner-builder-home-loans">Video – Why We Specialize in Owner Builder Home Loans</a></li>
<li class="page_item page-item-8626"><a href="https://www.intellichoice.com.au/what-are-construction-loans">What are Construction Loans?</a></li>
<li class="page_item page-item-8601"><a href="https://www.intellichoice.com.au/what-is-construction-loans">What is Construction Loans?</a></li>
<li class="page_item page-item-8622"><a href="https://www.intellichoice.com.au/what-is-smsf-self-managed-superannuation-fund">What is SMSF (Self-Managed Superannuation Fund)?</a></li>
</ul>
<h2 class="wsp-posts-title">Posts by category</h2>
<ul class="wsp-posts-list">
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/asset-finance-articles">Asset Finance Articles</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/what-is-the-best-source-for-equipment-financing-for-startup">What is the Best Source for Equipment Financing for Startup?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/what-are-the-loan-types-available-with-asset-finance">What Are The Loan Types Available with Asset Finance?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/what-is-asset-finance">What is Asset Finance?</a></li>
</ul></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/bad-credit-car-loan-videos">Bad Credit Car Loan Videos</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/what-is-needed-to-complete-or-finalise-your-bad-credit-car-loan">What is Needed to Complete or Finalise Your Bad Credit Car Loan</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/the-requirements-needed-when-applying-for-a-bad-credit-car-loan">The Requirements Needed for Bad Credit Car Loans Application</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-bad-credit-car-loans-have-been-used-by-others-previously">How Bad Credit Car Loans have been Used by Others Previously</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/what-is-a-bad-credit-car-loan">What Is A Bad Credit Car Loan?</a></li>
</ul></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/bad-credit-car-loans-articles">Bad Credit Car Loans Articles</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/car-loan-refinance-loans-for-people-with-bad-credit">Car Loan Refinance 2019: Loans for People with Bad Credit</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-to-secure-the-best-car-finance-rates-in-australia">How to Secure the Best Car Finance Rates in Australia</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/apply-for-a-car-loan-fast-how-a-loan-specialist-helps">Apply for a Car Loan Fast: How a Loan Specialist Helps</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/bad-credit-car-loan-dealerships-is-this-the-best-option-for-you">Bad Credit Car Loan Dealerships: Is This the Best Option for You?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/pre-approved-car-loan-advantages-and-disadvantages">Pre Approved Car Loan: Advantages and Disadvantages</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/car-loans-with-bad-credit-are-you-qualified">Car Loans with Bad Credit: Are You Qualified?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/second-chance-finance-personal-car-loans">Second Chance Finance Personal Car Loans</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-soon-can-you-apply-for-a-car-refinance-with-bad-credit">Perfect Timing: Apply for a Car Refinance with Bad Credit?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-easy-is-it-to-access-a-car-loan-in-australia">How Easy Is It to Access A Car Loan in Australia?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/5-steps-in-repairing-bad-credit-for-guaranteed-bad-credit-car-loans-approval">5 Steps in Repairing Bad Credit for Guaranteed Bad Credit Car Loans Approval</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-to-get-car-financing-with-a-low-credit-score-in-2018">Get Car Financing with A Low Credit Score in 2019</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/cheap-car-loans-how-affordable-are-they">Cheap Car Loans: How Affordable Are They?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-to-get-a-competitive-rate-for-your-car-loan-application">How to Get a Competitive Rate for Your Car Loan Application</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/buying-a-car-with-bad-credit-and-no-money-down">Buying a Car With Bad Credit and No Money Down</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/car-loan-with-bad-credit-how-fast-can-you-get-a-loan-approved">Car Loan With Bad Credit: How Fast Can You Get a Loan Approved</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/car-loans-with-bad-credit-refinance-when-is-the-right-time">Car Loans with Bad Credit Refinance: When Is the Right Time</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-to-finance-a-car-loan-with-bad-credit">How to Finance a Car Loan With Bad Credit</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/bad-credit-car-loans-from-private-sellers-how-do-they-work">Bad Credit Car Loans from Private Sellers: How Do They Work?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/my-bad-credit-car-loan-was-rejected-whats-my-next-step">My Bad Credit Car Loan Was Rejected: What’s My Next Step?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/bad-credit-car-financing-faqs-answers-to-your-common-bad-credit-car-loan-questions">Bad Credit Car Financing FAQs: Answers to Your Common Bad Credit Car Loan Questions</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/loans-for-people-with-bad-credit-bad-credit-mortgages-and-financing">Loans for People With Bad Credit:  Bad Credit Mortgages and Financing</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/bad-credit-car-finance-advantages-of-a-second-chance-car-loan">Bad Credit Car Finance: Advantages of a Second Chance Car Loan</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/top-11-tips-to-follow-for-bad-credit-car-loans-guaranteed-approval">Top 11 Tips to Follow for Bad Credit Car Loans Guaranteed Approval</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/determining-your-buying-power-can-you-afford-a-car-loan">Determining Your Buying Power: Can You Afford A Car Loan?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/i%D1%95-it-%D1%80%D0%BE%D1%95%D1%95%D1%96bl%D0%B5-to-get-a-car-l%D0%BE%D0%B0n-with-b%D0%B0d-credit">Iѕ It Pоѕѕіblе To Get Car Lоаns With Bаd Credit?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/what-are-the-pros-and-cons-of-car-loans">What are the Pros and Cons of Car loans?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/what-is-a-car-loan">What is a Car Loan?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/can-buy-car-defaults-credit-file">Can I Buy a Car with Defaults on My Credit File?</a></li>
</ul></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/broker-specialist">Broker Specialist</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/why-do-i-need-a-mortgage-broker-to-get-a-home-loan">Why Do I Need a Mortgage Broker to Get A Home Loan?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/why-use-broker-specialist">Why use Broker Specialist?</a></li>
</ul></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/business-finance">Business Finance</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/business-financing-which-one-is-best-for-you">Business Financing: Which One Is Best for You?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/what-is-needed-to-apply-for-a-business-loan">What Is Needed to Apply for A Business Loan</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/funding-and-loans-for-your-business-which-one-is-for-you">Funding and Loans for Your Business: Which One is For You?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-to-get-an-unsecured-business-loan-in-australia">How to Get an Unsecured Business Loan in Australia</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/understanding-the-difference-between-leasing-finance-and-operating-finance">Understanding the Difference Between Leasing Finance and Operating Finance</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/types-of-business-loans-which-one-is-for-you">Types of Business Loans: Which One is For You?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/what-is-commercial-property-finance">What is Commercial  Property Finance?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/supply-chain-finance-how-it-helps-a-thriving-business">Supply Chain Finance: How It Helps a Thriving Business</a></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/business-finance/business-finance-videos">Business Finance Videos</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/expatriate-and-foreign-national-purchasers-understanding-why-intellichoice-digs-deeper-into-providing-mortgages-for-you">Expatriate and Foreign National Purchasers; Understanding Why Intellichoice Digs Deeper into providing Mortgages for You</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/financing-your-business-understanding-available-options">Financing Your Business: Understanding Available Options</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/specialist-business-finance-how-equipment-and-asset-has-to-be-considered">Specialist Business Finance-How Equipment and Asset has to be Considered</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/understanding-how-intellichoice-approaches-short-term-finance-for-their-clients">Understanding How Intellichoice Approaches Short Term Finance For Their Clients</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/intellichoice-financial-services-why-people-use-us">Expatriates-We Really Understand Your Mortgage Needs!</a></li>
</ul></li>
</ul></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/car-loans">Car Loans</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-to-secure-the-cheapest-car-loans-in-australia">How to Secure the Cheapest Car Loans in Australia</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/better-car-financing-regulation-favors-australian-buyers">Better Car Financing Regulation Favors Australian Buyers</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/car-loan-vs-novated-lease-whats-the-difference">Car Loan vs Novated Lease: What’s the Difference?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-to-avail-the-cheapest-car-loans-in-australia">How to Avail the Cheapest Car Loans in Australia</a></li>
</ul></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/construction-loans-articles">Construction Loans Articles</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-do-land-and-construction-loans-works">How Do Land and Construction Loans Works</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-to-make-your-home-construction-a-success">How to Make Your Home Construction a Success</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-to-build-your-own-house-through-a-mortgage">How to Build Your Own House Through a Mortgage</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/your-ultimate-guide-to-construction-loans-australia-2018">Your Ultimate Guide to Construction Loans Australia 2019</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/the-construction-route-for-your-home-is-your-builder-legit">The Construction Route for Your Home: Is Your Builder Legit?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/construction-loans-explained-how-do-they-work">Construction Loans Explained: How Do They Work?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/owner-built-home-good-builder">Defining a Good Owner Builder: Which Contractor is Perfect for Your Owner-Built</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-does-the-process-work-at-intellichoice">How Does the Process Work at Intellichoice?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/are-building-loans-the-right-choice-for-you">Are building loans the right choice for you?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/why-your-project-needs-to-be-financed-with-a-construction-home-loan">Why Your Project Needs to be Financed with a Construction Home Loan</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-construction-home-loans-work">How Construction Home Loans Work</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/why-do-you-need-to-know-about-owner-builder-construction-loans">Why do you need to know about owner builder construction loans?</a></li>
</ul></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/equipment-finance">Equipment Finance</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-to-apply-for-a-bad-credit-equipment-finance">How to Apply for a Bad Credit Equipment Finance</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/equipment-financing-means-flexible-solutions-for-unique-business-needs">Equipment Financing Means Flexible Solutions for Unique Business Needs</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/for-borrowers-with-credit-histories-that-may-have-black-mark-associated-with-them">For Borrowers With Credit Histories that May Have Black Mark Associated with Them</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/types-of-equipment-finance-options">Types of Equipment Finance Options</a></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/equipment-finance/equipment-finance-videos">Equipment Finance Videos</a></strong>
</li>
</ul></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/expat-foreign-owner-loans">Expat Foreign Owner Loans</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/australian-expat-home-loans-getting-a-home-loan-when-living-overseas">Australian Expat Home Loans: Getting a Home Loan When Living Overseas</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/questions-to-ask-before-getting-an-expat-foreign-home-loans">Questions to Ask Before Getting an Expat Foreign Home Loans</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-easy-it-is-to-access-a-home-loan-in-australia">How Easy it is to Access a Home Loan in Australia</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/its-still-possible-to-get-a-home-loan-to-buy-property-in-australia">It’s Still Possible to Get a Home Loan to Buy Property in Australia</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/invest-australian-property">Invest in Australian Property</a></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/expat-foreign-owner-loans/expat-foreign-owner-loans-videos">Expat Foreign Owner Loans Videos</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/expatriate-and-foreign-national-purchasers-buy-before-you-leave-or-while-living-and-working-away-from-oz">Expatriate and Foreign National Purchasers; Buy Before you Leave or While Living and Working Away from Oz</a></li>
</ul></li>
</ul></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/uncategorized">General</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/which-banks-in-australia-offers-95-lvr-home-loans">Which Banks in Australia Offers 95% LVR Home Loans?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/what-should-you-avoid-when-looking-for-bad-credit-car-loans">What Should You Avoid When Looking for Bad Credit Car Loans?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/should-i-pay-off-my-credit-card-or-personal-loan-first">Should I Pay Off my Credit Card or Personal Loan First?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/mortgage-house-for-sale-what-is-the-process">Mortgage House for Sale: What is the Process?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/top-9-tips-for-self-employed-mortgage-borrowers-in-australia">Top 9 Tips for Self-Employed Mortgage Borrowers in Australia</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-australian-expats-can-still-get-a-home-loan">How Australian Expats Can Still Get a Home Loan?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/what-should-i-look-for-in-a-car-finance">What Should I Look for in a Car Finance?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/why-you-need-to-keep-up-with-home-loan-repayments">Why You Need to Keep Up With Home Loan Repayments</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/what-are-the-requisites-for-a-real-estate-commercial-loan">What are the Requisites for a Real Estate Commercial Loan?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/moving-house-checklist-after-a-successful-home-loan">Moving House Checklist After a Successful Home Loan</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/top-reasons-why-you-need-to-get-a-general-insurance">Top Reasons Why You Need to Get a General Insurance</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-to-reduce-home-loan-rates">How to Reduce Home Loan Rates?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/pepper-money-loans-what-do-they-offer">Pepper Money Loans: What Do They Offer?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/what-are-existing-personal-loan-rates-in-australia">What are Existing Personal Loan Rates in Australia?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-to-use-an-lmi-calculator">How to Use an LMI Calculator</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/car-loans-brisbane">Car Loans Brisbane</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/business-loans-sydney">Business Loans Sydney</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/business-loans-melbourne">Business Loans Melbourne</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/business-loans-brisbane">Business Loans Brisbane</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/bad-credit-loans-guaranteed-approval-sydney">Bad Credit Loans Guaranteed Approval Sydney</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/bad-credit-loans-guaranteed-approval-melbourne">Bad Credit Loans Guaranteed Approval Melbourne</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/bad-credit-loans-guaranteed-approval-brisbane">Bad Credit Loans Guaranteed Approval Brisbane</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/bad-credit-home-loans-sydney">Bad Credit Home Loans Sydney</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/bad-credit-home-loans-brisbane">Bad Credit Home Loans Brisbane</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/bad-credit-home-loans-melbourne">Bad Credit Home Loans Melbourne</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/bad-credit-car-loans-sydney">Bad Credit Car Loans Sydney</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/bad-credit-car-loans-melbourne">Bad Credit Car Loans Melbourne</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/bad-credit-car-loans-brisbane">Bad Credit Car Loans Brisbane</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/asset-finance-sydney">Asset Finance Sydney</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/asset-finance-brisbane">Asset Finance Brisbane</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/asset-finance-melbourne">Asset Finance Melbourne</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-to-apply-for-emergency-cash-loans">How to Apply for Emergency Cash Loans</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/are-personal-loans-good-or-bad-debt">Are Personal Loans Good or Bad Debt?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/comprehensive-credit-reporting-and-its-effect-on-your-personal-finances">Comprehensive Credit Reporting and Its Effect on Your Personal Finances</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/why-you-need-a-compound-interest-calculator">Why You Need A Compound Interest Calculator</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/why-having-a-loan-set-up-with-experienced-brokers-is-a-lot-different-to-having-one-set-by-a-bank">Why having a Loan set up with Experienced Brokers is a lot different to having one set up by a Bank</a></li>
</ul></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/home-loan-articles-videos">Home Loans Articles and Videos</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-to-apply-for-a-refinance-home-loan">How to Apply for a Refinance Home Loan</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/buying-a-house-in-2019-what-you-need-to-know">Buying a House in 2019: What You Need to Know</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/basic-financial-considerations-for-the-first-home-buyer">Basic Financial Considerations For The First Home Buyer</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/investment-property-and-home-loans-how-are-they-connected">Investment Property and Home Loans: How Are They Connected?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/stamp-duty-calculator-for-2019">Stamp Duty Calculator for 2019</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/mortgage-calculator-how-to-use-before-applying-for-a-loan">Mortgage Calculator: How to Use Before Applying for a Loan</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/lvr-calculator-how-it-can-help">LVR Calculator: How it Can Help</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/is-it-possible-to-get-a-second-mortgage-in-australia">Is it Possible to Get a Second Mortgage in Australia?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/what-makes-home-loan-brokers-beneficial-in-purchasing-a-new-home">What Makes Home Loan Brokers Beneficial in Purchasing a New Home?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/what-is-reverse-mortgage-is-it-ideal-for-you">What is Reverse Mortgage? Is it Ideal for You?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/home-equity-loan-and-investing-how-do-they-work">Home Equity Loan and Investing: How Do They Work</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-to-use-equity-in-buying-investment-property">How to Use Equity in Buying Investment Property</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/90-home-loan-lenders-applying-for-mortgage-in-australia">90% Home Loan Lenders: Applying for Mortgage in Australia</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/discounts-on-home-loan-rates-how-to-avail">Discounts on Home Loan Rates: How to Avail</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/what-are-the-requirements-of-basic-aussie-home-loans-2018">What Are The Requirements of Basic Aussie Home Loans 2019?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/no-doc-home-loans-australia-how-to-apply-and-qualify">No Doc Home Loans Australia: How to Apply and Qualify</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/my-bad-credit-home-loan-is-rejected-what-do-i-do-next">My Bad Credit Home Loan is Rejected: What Do  I Do Next?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/real-estate-investing-steps-to-make-it-a-success">Real Estate Investing: Steps to Make it a Success</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/home-loan-repayment-calculator-whats-the-actual-cost-of-your-mortgage">Home Loan Repayment Calculator: What’s the Actual Cost of Your Mortgage?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/getting-a-home-loan-how-long-does-it-takes">Getting a Home Loan: How Long Does it Takes?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/steps-in-applying-for-investment-property-loans">Steps in Applying for Investment Property Loans</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-to-compare-home-loan-rates-effectively">How to Compare Home Loan Rates Effectively</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/making-credit-easier-to-obtain">Why Getting A Home Loan has Become a Lot More Thorough Recently</a></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/home-loan-articles-videos/95-home-loans">95 Home Loans</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/95-home-loans-a-5-deposit-mortgage">95 Home Loans: A 5% Deposit Mortgage</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/what-is-lenders-mortgage-insurance">What is Lenders Mortgage Insurance?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/low-deposit-home-loans-is-this-the-right-mortgage-for-you">Low Deposit Home Loans: Is This The Right Mortgage for You?</a></li>
</ul></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/home-loan-articles-videos/bad-credit-home-loan-category">Bad Credit Home Loan</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/when-is-the-right-time-to-apply-for-a-home-loan">When is the Right Time to Apply for a Home Loan?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-to-use-a-bad-credit-home-loan-calculator">How to Use a Bad Credit Home Loan Calculator</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/why-do-you-need-to-hire-a-bad-credit-home-loan-broker">Why Do You Need to Hire a Bad Credit Home Loan Broker?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/why-do-you-need-to-get-a-bad-credit-home-loan-broker">Why Do You Need to Get a Bad Credit Home Loan Broker?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/can-you-buy-a-house-with-bad-credit-before-christmas-2018">Can You Buy a House with Bad Credit before Christmas 2018?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/home-loan-options-for-people-with-bad-credit">Home Loan Options for People with Bad Credit</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/5-tips-for-first-time-home-buyers-with-bad-credit">5 Tips For First Time Home Buyers with Bad Credit</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/best-solution-to-acquire-your-dream-home-bad-credit-home-loans-in-australia">Best Solution to Acquire Your Dream Home – Bad Credit Home Loans in Australia</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/bad-credit-home-loans-in-australia">Bad Credit Home Loans in Australia</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/purchasing-your-own-home-is-an-important-life-milestone-for-many-people">Purchasing Your Own Home is an Important Life Milestone for Many People</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/minor-default-can-turn-off-lenders">How a Minor Default can turn off Lenders</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/bad-credit-home-loans-unjust-bad-credit-file">Unjust Bad Credit File | Bad Credit Home Loans</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/need-good-credit-get-home-loan">Do I need Good Credit to get a Home Loan</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/tips-maintaining-credit-file">Tips for Maintaining your Credit File</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/can-unpaid-defaults-credit-file">What Can I do about unpaid defaults on my credit file</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/can-still-get-loan-bad-credit">Can I still get a loan with bad credit?</a></li>
</ul></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/home-loan-articles-videos/fixed-home-loan-articles">Fixed Home Loan Articles</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/a-combination-or-split-home-loans-allows-you-to-customize-the-home-loan">A Combination or Split Home Loans Allows You to Customize the Home Loan</a></li>
</ul></li>
</ul></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/insurance">Insurance</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/5-things-to-consider-when-choosing-the-right-home-insurance">5 Things to Consider when Choosing the Right Home Insurance</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/reason-why-you-should-get-life-insurance">Reason Why You Should Get Life Insurance</a></li>
</ul></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/inventory-finance">Inventory Finance</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/best-inventory-loans-for-your-business-2018">Best Inventory Loans for Your Business 2019</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/what-is-inventory-finance">What is Inventory Finance</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/pros-cons-inventory-finance">What are the Pros and Cons of Inventory Finance</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/inventory-finance-basics">Inventory Finance The Basics</a></li>
</ul></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/investment-and-advice">Investment and Advice | Category</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/top-15-investment-advice-from-real-estate-experts">Top 15 Investment Advice from Real Estate Experts</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/thank-making-dreams-come-true">Thank you for making my dreams come true</a></li>
</ul></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/invoice-finance">Invoice Finance</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/find-right-invoice-finance">Find the Right Invoice Finance</a></li>
</ul></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/low-doc-construction-loans-articles">Low Doc Construction Loans Articles</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/requirements-for-owner-builder-home-loans-2018">Requirements for Owner Builder Home Loans 2019</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/low-doc-construction-home-loans-step-by-step-guide-for-application">Low Doc Construction Home Loans Step by Step Guide for Application</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/h%D0%BEw-t%D0%BE-get-a-m%D0%BErtg%D0%B0g%D0%B5-with%D0%BEut-d%D0%BE%D1%81um%D0%B5nt%D0%B5d-in%D1%81%D0%BEm%D0%B5">Hоw tо Get a Mоrtgаgе Withоut Dосumеntеd Inсоmе</a></li>
</ul></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/owner-builder-home-loan">Owner Builder Home Loan</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-owner-builders-can-secure-a-mortgage-loan">How Owner Builders Can Secure A Mortgage Loan</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-to-become-and-owner-builder-in-australia">How to Become and Owner Builder in Australia</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/ultimate-guide-to-owner-builder-home-loans">Ultimate Guide to Owner Builder Home Loans 2019</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/owner-builder-financing-road-faqs-answered">Owner-Builder Financing Road: FAQs Answered</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/should-you-consider-taking-an-owner-builder-construction-loans">Should You Consider Taking An Owner-Builder Construction Loans?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/is-it-better-to-get-loan-from-the-bank-or-from-the-broker">Is It Better to Get Loan From the Bank or from the Broker?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/why-is-an-owner-builder-home-loan-different">Why is an Owner Builder Home Loan Different?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/owner-builder-finance-information">Owner Builder Finance Information</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/owner-builder-loans-how-it-works-benefits-things-to-consider">Owner Builder Loans: How it Works, Benefits, Things to Consider</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/why-is-it-difficult-to-get-loans-for-an-owner-builder-project">Why is it Difficult to Get Loans for an Owner Builder Project?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/what-is-the-situation-with-owner-builders-in-queensland">What is the Situation with Owner Builders in Queensland?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/why-are-the-cost-savings-so-significant-when-you-owner-build">Why are the cost savings so significant when you Owner Build?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/not-everyone-is-as-passionate-about-owner-builder-loans-as-jo-king-of-intellichoice">Not everyone is as passionate about Owner Builder Loans as Jo King of Intellichoice</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/why-should-i-use-intellichoice">Why Should I Use Intellichoice?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/top-tips-for-successfully-owner-building-a-project">Top Tips for Successfully Owner Building a Project</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/why-do-banks-value-owner-builder-projects-differently">Why Do Banks Value Owner Builder Projects Differently?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/what-do-i-need-to-know-about-insurance-for-owner-builders">What Do I Need to Know About Insurance for Owner Builders</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/can-i-use-my-normal-home-loan-to-be-an-owner-builder">Can I Use My Normal Home Loan to Be an Owner Builder?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/save-a-fortune-and-build-your-own-home-as-an-owner-builder">Save a Fortune and Build your Own Home as an Owner Builder</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/is-it-hard-to-get-finance-as-an-owner-builder">Is it Hard to Get Finance as an Owner Builder?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/dont-become-an-owner-builder-without-the-right-finance">Don’t Become an Owner Builder Without the Right Finance</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/what-are-staged-payments-of-building-loans">What are Staged Payments of Building Loans?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/which-owner-builder-construction-loan-is-right-for-me">Which owner builder construction loan is right for me?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/building-construction-buildings">Building Construction Buildings</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/becoming-an-owner-builder">Becoming an Owner-Builder</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/intellichoice-much-research-owner-builder-home-loans">Why does Intellichoice do so much research for their Owner Builder Home Loans?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/people-owner-builder">Why do People Owner Builder</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/whats-really-like-owner-builder">What’s It Like to Be an Owner Builder?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/real-story-owner-builder-finance">The real story about Owner Builder Finance</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/find-owner-builder-home-loans">Find an Owner Builder Home Loans</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/thinking-becoming-owner-builder">Thinking about becoming an owner builder?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/owner-builder-affordable-option">The Affordable Option For Owner Builder Projects</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/requirements-owner-builder-loan">Requirements for an Owner Builder Loan</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/owner-builder-renovations">Owner Builder Renovations</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/tale-unprepared-owner-builder">The Tale of an Unprepared Owner Builder</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/not-everyone-love-owner-builder-loans-like">Not everyone love Owner Builder Loans like we do</a></li>
</ul></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/owner-builder-loans-video">Owner Builder Loans Video</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/why-our-ceo-was-always-so-interested-in-helping-what-most-lenders-consider-too-hard-basket-owner-builder-clients">Intellichoice vs The Banks: Too Hard Basket’ Owner Builder Loans Clients</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/owner-builder-loan">Intellichoice Provides Examples of the Most Commonly Asked Questions Regarding Funds from an Owner builder Loan</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/darin-from-intellichoice-talks-of-the-process-for-owner-builder-loans-and-why-a-specialist-is-needed">Darin from Intellichoice talks of the process for Owner-Builder Loans-and why a specialist is needed</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/making-the-process-for-owner-building-and-owner-builder-lending-easier">Making the Process for Owner Building and Owner Builder Lending Easier</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/intellichoice-owner-builder-loan-stages">Owner Builder Loan Stages: Understanding the Intellichoice Process</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/owner-builder-loans-difference">Understanding why Intellichoice Owner Builder Loans differ from Traditional Loans</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/intellichoice-owner-builder-loans-end-market-value-importance">Intellichoice Explains the Importance of Understanding End Market Value for an Owner Builder</a></li>
</ul></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/personal-finance">Personal Finance</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/get-your-finances-straight-with-an-income-calculator">Get Your Finances Straight With An Income Calculator</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/what-does-my-credit-score-say-about-my-finances">What Does My Credit Score Say About My Finances</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/no-credit-check-loans-are-they-for-real">No Credit Check Loans: Are They For Real?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/how-to-improve-your-credit-score">How to Improve Your Credit Score</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/small-loans-to-help-your-immediate-financial-needs">Small Loans to Help Your Immediate Financial Needs</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/what-are-personal-bank-loans">What are Personal Bank Loans?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/secured-loans-apply-australia">Secured Loans You Can Apply for in Australia</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/secured-loans-you-can-apply-for-in-australia">Secured Loans You Can Apply for in Australia</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/pros-and-cons-of-cash-loans-for-unemployed">Pros and Cons of Cash Loans for Unemployed</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/personal-loans-australia-borrowing-options-you-can-avail">Personal Loans Australia: Borrowing Options You Can Avail</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/can-you-have-multiple-personal-loans-at-the-same-time">Can You Have Multiple Personal Loans at the Same Time?</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/things-you-will-need-to-think-about-when-applying-for-a-personal-loan">Things You Will Need to Think About When Applying for a Personal Loan</a></li>
</ul></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/personal-loans">Personal Loans</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/understanding-personal-loans-australia-2019">Understanding Personal Loans Australia 2019</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/personal-loans-comparing-for-the-right-choice">Personal Loans: Comparing for the Right Choice</a></li>
</ul></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/self-managed-super-fund-loans">Self Managed Super Fund Loans</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/buying-a-property-with-your-superannuation-pros-and-cons">Buying a Property with Your Superannuation: Pros and Cons</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/smsf-can-work-current-climate">How SMSF can work in the current climate</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/lending-self-managed-super-funds">Lending for Self Managed Super Funds</a></li>
</ul></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/trade-finance">Trade Finance</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/why-trade-finance-an-empirical-business-solution">Why Trade Finance? an Empirical Business Solution</a></li>
		<li class="wsp-post"><a href="https://www.intellichoice.com.au/find-right-trade-finance">Find the Right Trade Finance</a></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/trade-finance/trade-finance-videos">Trade Finance Videos</a></strong>
<ul class="wsp-posts-list">		<li class="wsp-post"><a href="https://www.intellichoice.com.au/intellichoice-trade-finance">Understanding How Intellichoice Approaches Trade Finance for their Clients</a></li>
</ul></li>
</ul></li>
	<li><strong class="wsp-category-title">Category: <a href="https://www.intellichoice.com.au/category/video">Video</a></strong>
</li>
</ul>
<h2 class="wsp-popups-title">Popups</h2>
<ul class="wsp-popups-list">
<li><a href="https://www.intellichoice.com.au/popup/owner-builder-home-loan-setting-the-deal">Owner Builder Home Loan - Setting the Deal</a></li>
<li><a href="https://www.intellichoice.com.au/popup/owner-builder-home-loan-the-paperwork">Owner Builder Home Loan - The Paperwork</a></li>
<li><a href="https://www.intellichoice.com.au/popup/owner-builder-home-loan-the-scenarios">Owner Builder Home Loan - The Scenarios</a></li>
<li><a href="https://www.intellichoice.com.au/popup/owner-builder-home-loan-the-explainer">Owner Builder Home Loan - The Explainer</a></li>
<li><a href="https://www.intellichoice.com.au/popup/what-is-needed-to-complete-or-finalise-your-bad-credit-asset-finance">What is Needed to Complete or Finalise Your Bad Credit Asset Finance</a></li>
<li><a href="https://www.intellichoice.com.au/popup/the-requirements-needed-when-applying-for-a-bad-credit-asset-finance">The Requirements Needed When Applying for a Bad Credit Asset Finance</a></li>
<li><a href="https://www.intellichoice.com.au/popup/bad-credit-asset-finance-how-it-can-help">Bad Credit Asset Finance - How It Can Help</a></li>
<li><a href="https://www.intellichoice.com.au/popup/bad-credit-asset-finance-what-is-it">Bad Credit Asset Finance - What is it</a></li>
<li><a href="https://www.intellichoice.com.au/popup/bccl-deal">bccl deal</a></li>
<li><a href="https://www.intellichoice.com.au/popup/bccl-requirements">bccl requirements</a></li>
<li><a href="https://www.intellichoice.com.au/popup/bccl-used-previously">bccl used previously</a></li>
<li><a href="https://www.intellichoice.com.au/popup/bccl-explainer">bccl explainer</a></li>
</ul>
</div>
"""


soup = BeautifulSoup(text.encode('utf-8'), 'html.parser')
posts = soup.find_all(class_='page_item')

with open('pages.csv', 'w', newline='') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['id', 'title', 'body', 'author', 'slug']
    csv_writer.writerow(headers)

    id = 0
    for post in posts:
        title = post.get_text().replace('\n', '')
        #title = post.get_text()
        link = post.find('a')['href']
        link_split = link.split('/')
        url = link_split[-1]
        body = ''
        author = 'Darin Hindmarsh'
        rows = [id, title, body, author, url]
        id += 1
        csv_writer.writerow(rows)
