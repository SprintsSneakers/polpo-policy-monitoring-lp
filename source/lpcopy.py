# Copy for the Polpo trial landing page, v2.
# Client copy IDs (H01, C01, ...) come from Polpo_AI_Copy_Spec_EN_NL_BE.json.
# Lines without an ID are S&S additions (structure from the Canva feedback).

EN = dict(
    lang="en", html_lang="en", path="/", other_path="/nl-be/",
    sw_self="EN", sw_other="NL", sw_other_label="Nederlands (België)",
    title="Polpo trial | Political monitoring set up for you",                      # M01
    desc="Get a Polpo trial with searches and alerts tailored to your topic. Complete the form, attend a 30-minute onboarding session and start monitoring after handover.",  # M02 (changed by S&S, deviates from spec)
    og_locale="en_GB",
    nav_how="How it works", nav_ready="What is ready", nav_faq="Questions",
    eyebrow="Made for Public Affairs teams.",
    h1=["Policy monitoring.", "Built for you."],                                    # H01 (changed by S&S, deviates from spec)
    h2="Get personalised monitoring of your topics, know what’s changed, understand what it means, and access the original sources behind every update.",  # H02 (changed by S&S, deviates from spec)
    cta="Get started",                                                                # C01 (changed by S&S, deviates from spec)
    cta2="How it works",                                                              # C02
    wins=["Set up for your topic", "A 30-minute onboarding session", "Monitoring active after handover"],  # H03 (changed by S&S, deviates from spec)
    vert_label="Monitoring for",
    verts=[("\U0001F1EA\U0001F1FA", "EU", "European Union"), ("\U0001F1E7\U0001F1EA", "Belgium", "Belgium"),
           ("\U0001F1F3\U0001F1F1", "Netherlands", "Netherlands"), ("\U0001F1F1\U0001F1FA", "Luxembourg", "Luxembourg")],
    logos_cap="Organisations monitoring with Polpo",
    # process (MAP04)
    p_head="Your monitor, ready in two steps",                                        # P01
    step_lab="Step",
    steps=[("Tell us what you follow",                                                # P02
            "Share your policy topic. We’ll tailor your searches and alerts.",        # P03 (changed by S&S)
            "Your topic", "EU sustainable packaging"),
           ("Monitor handover",                                                       # P04 (changed by S&S)
            "We’ll walk you through your tailored monitor together, so you’re ready to start tracking.",  # P05 (changed by S&S, deviates from spec)
            "Your trial account", "Searches and alerts ready")],
    # value (MAP02)
    v_head=["All the answers you need.", "In one place."],                            # V01 (changed by S&S, deviates from spec)
    v_body=["Imagine all the policy topics you follow, relevant developments and alerts, all organised around your priorities."],  # V02 (changed by S&S, deviates from spec)
    # benefits (MAP03)
    b_head="What is ready for you",                                                   # B00
    bcards=[("Searches tailored to your topic", "See relevant policy developments in one place, without searching multiple sources."),
            ("Updates delivered to your inbox", "Get alerts when new developments match your priorities."),
            ("Ready to go in 30 minutes", "We’ll walk you through your setup so you can start monitoring with confidence."),
            ("You’re always in control", "Fine-tune your searches and alerts as your priorities change.")],  # B01-B04 (changed by S&S)
    mock_head="Your trial account",
    mock_tags=["Example", "Prepared by Polpo"],
    mock_rows=[("Topic", "EU rules on sustainable packaging"),
               ("Saved searches", "packaging waste, PPWR, recycled content, producer responsibility"),
               ("Email alerts", "Daily summary, adjustable"),
               ("Level", "European Union, scope agreed with you")],
    # without / with (Canva)
    d_eyebrow="The difference",
    d_head="Transform how you monitor policy.",
    d_sub="See what changes once your topic is being monitored for you.",
    d_without="Without Polpo",
    d_with="With Polpo",
    d_wo=["You spend hours checking official sources for updates.",
          "You have to dig through lengthy documents to find what actually matters.",
          "You scramble for answers when stakeholders ask for an update."],
    d_w=["Everything on your topic, in one place.",
         "Email alerts when something important changes.",
         "You get stakeholder-ready answers, linked to original sources."],
    d_close="Your time goes to shaping policy, not chasing it.",
    # form (MAP07)
    f_head="Tell us what you want to monitor",                                        # F01
    f_intro="We’ll use your answer to build a monitor tailored to your needs and schedule your free onboarding session.",  # F02 (changed by S&S, deviates from spec)
    step_of="Step {n} of {t}",
    l_dossier="What would you like to monitor?",                                      # F12
    ph_dossier="e.g. EU packaging rules",
    sugs_label="Often asked for:",
    sugs=["AI Act", "CBAM", "Packaging rules", "Energy policy", "ETS reform"],
    l_context="What matters to your organisation?", optional="optional",
    ph_context="For example: EU rules on sustainable packaging — policy proposals and committee discussions relevant to packaging producers.",  # F13
    help_context="Tell us what matters to your organisation. Add relevant institutions or exclusions if useful. No search query needed.",  # F14 (changed by S&S, topic moved to its own step)
    b_continue="Continue", b_back="Back",
    l_level="Which politics do you follow?",                                          # F07
    sr_pick="Pick one.",
    lvl={"EU": "European Union", "NL": "Netherlands", "BE": "Belgium"},               # F08-F10
    lvl_order=["EU", "BE", "NL"],
    echo_default="Last step. We contact you on your work email to plan the onboarding session.",
    echo_with="Last step, then we start preparing <b></b> for you.",
    l_name="Name", ph_name="Your name",
    l_email="Work email", ph_email="you@company.com",                                 # F05
    consent='I consent to Polpo using my answers to create my trial account and contact me, in line with the <a href="https://polpo.com/privacy-policy/">Privacy Policy</a>.',  # (changed by S&S, deviates from spec)
    submit="Get started",                                                             # F15 (changed by S&S, deviates from spec)
    sending="Sending…",
    e_dossier="Tell us which topic you would like to monitor.",                        # E01
    e_level="Pick the level you follow this topic at.",
    e_name="We need a name for your account.",
    e_email="Enter a valid email address.",                                            # E02
    e_consent="We need your go-ahead to prepare your account and contact you.",
    e_form="Your request was not sent. Please try again.",                             # E03
    done_t="Your request is received",                                                 # T01
    done_b="We’ll prepare your trial around the topic you shared and contact you to arrange your 30-minute onboarding session. During the session, we’ll review the setup and hand over your account. Your monitoring starts afterwards.",  # T02 (changed by S&S, deviates from spec)
    perk="Free 1:1 onboarding included",
    reassure="Your details stay private.",
    faq_head="Frequently asked questions",
    faq=[("What will I receive?", "A Polpo trial account with saved searches and email alerts configured around your topic. We review the setup with you and hand over access during the 30-minute onboarding session."),
         ("What happens after I complete the form?", "We use your answers to prepare your account and arrange the onboarding session with you. Submitting the form requests your trial; monitoring starts after the onboarding session and account handover."),
         ("Why is the onboarding session included?", "The session is held in your own prepared account. We check your topic and alert settings, show you how to use and adjust the monitor, and give you access to continue independently."),
         ("When will I receive updates?", "Monitoring starts immediately after handover. An email alert is sent when matching information is available, according to your alert settings. The first new alert therefore depends on relevant publications and your chosen frequency."),
         ("Can I change my topic or alerts?", "Yes. You can adjust your saved searches and alert preferences yourself. We show you how during the onboarding session."),
         ("Which political sources are included?", "We agree the relevant institutions and available sources for your topic when preparing the account. You can see the selected sources in your trial."),
         ("What happens to my details?", "Your name, work email and topic go to Polpo so we can prepare your account and plan the onboarding session. We do not sell or pass them on. Every email carries an unsubscribe link and we delete your details whenever you ask.")],
    z_head="Let’s set up your monitor",                                               # Z01 (changed by S&S, deviates from spec)
    z_body="Share your topic. We’ll prepare the setup and show you how to use it in your 30-minute onboarding session.",  # Z02 (changed by S&S, deviates from spec)
    sticky="Searches and alerts prepared for your topic.",
    foot_tag="AI-powered political monitoring", polpo_url="https://polpo.com/",
)

NL = dict(
    lang="nl-BE", html_lang="nl-BE", path="/nl-be/", other_path="/",
    sw_self="NL", sw_other="EN", sw_other_label="English",
    title="Polpo-proefaccount | Belgische politieke monitoring",                       # M01
    desc="Vraag je Polpo-proefaccount aan met zoekopdrachten en meldingen op maat. Na je onboardingsessie van 30 minuten start je Belgische politieke monitoring.",  # M02 (changed by S&S, deviates from spec)
    og_locale="nl_BE",
    nav_how="Zo werkt het", nav_ready="Wat staat klaar", nav_faq="Vragen",
    eyebrow="Gemaakt voor Public Affairs-teams.",  # EN now says "Made for", NL already did
    h1=["Beleidsmonitoring.", "Voor jou gebouwd."],                                  # H01 (changed by S&S, deviates from spec)
    h2="Volg je dossiers op maat, zie wat er veranderd is, begrijp wat het betekent en raadpleeg de originele bronnen achter elke update.",  # H02 (changed by S&S, deviates from spec)
    cta="Aan de slag",                                                                # C01 (changed by S&S, deviates from spec)
    cta2="Zo werkt het",                                                              # C02
    wins=["Ingesteld op jouw dossier", "Een onboardingsessie van 30 minuten", "Monitoring actief na de overdracht"],  # H03 (changed by S&S, deviates from spec)
    vert_label="Monitoring voor",
    verts=[("\U0001F1EA\U0001F1FA", "EU", "Europese Unie"), ("\U0001F1E7\U0001F1EA", "België", "België"),
           ("\U0001F1F3\U0001F1F1", "Nederland", "Nederland"), ("\U0001F1F1\U0001F1FA", "Luxemburg", "Luxemburg")],
    logos_cap="Organisaties die met Polpo monitoren",
    p_head="Jouw monitor in twee stappen",                                            # P01
    step_lab="Stap",
    steps=[("Vertel ons wat je opvolgt",                                              # P02
            "Geef je beleidsdossier door. Wij stemmen je zoekopdrachten en meldingen daarop af.",  # P03 (changed by S&S)
            "Jouw dossier", "Energiebeleid voor Belgische bedrijven"),
           ("Overdracht van je monitor",                                              # P04 (changed by S&S)
            "We lopen je monitor op maat samen door, zodat je meteen kunt beginnen met volgen.",  # P05 (changed by S&S, deviates from spec)
            "Jouw proefaccount", "Zoekopdrachten en meldingen klaar")],
    v_head=["Alle antwoorden die je nodig hebt.", "Op één plek."],                    # V01 (changed by S&S, deviates from spec)
    v_body=["Stel je voor: alle beleidsdossiers die je opvolgt, de relevante ontwikkelingen en de meldingen, geordend rond jouw prioriteiten."],  # V02 (changed by S&S, deviates from spec)
    b_head="Wat staat er voor je klaar?",                                             # B00
    bcards=[("Zoekopdrachten op maat van jouw dossier", "Zie relevante beleidsontwikkelingen op één plek, zonder meerdere bronnen af te gaan."),
            ("Updates in je mailbox", "Krijg een melding zodra nieuwe ontwikkelingen aansluiten op jouw prioriteiten."),
            ("Klaar voor gebruik in 30 minuten", "We nemen je inrichting met je door, zodat je met vertrouwen aan je monitoring begint."),
            ("Jij houdt de controle", "Verfijn je zoekopdrachten en meldingen wanneer je prioriteiten veranderen.")],  # B01-B04 (changed by S&S)
    mock_head="Jouw proefaccount",
    mock_tags=["Voorbeeld", "Voorbereid door Polpo"],
    mock_rows=[("Dossier", "Energiebeleid voor Belgische bedrijven"),
               ("Zoekopdrachten", "energienorm, netkosten, energieprijzen bedrijven, energietransitie"),
               ("E-mailmeldingen", "Dagelijks overzicht, aanpasbaar"),
               ("Niveau", "Federaal en Vlaams, afbakening samen bepaald")],
    d_eyebrow="Het verschil",
    d_head="Verander hoe je beleid opvolgt.",
    d_sub="Zie wat er verandert zodra je dossier voor jou wordt opgevolgd.",
    d_without="Zonder Polpo",
    d_with="Met Polpo",
    d_wo=["Je bent uren bezig met het nakijken van officiële bronnen.",
          "Je moet lange documenten doorploegen om te vinden wat er echt toe doet.",
          "Je zoekt in allerijl naar antwoorden wanneer een stakeholder om een update vraagt."],
    d_w=["Alles over jouw dossier, op één plek.",
         "E-mailmeldingen zodra er iets belangrijks verandert.",
         "Antwoorden die je meteen kunt delen, met een link naar de bron."],
    d_close="Zo gaat je tijd naar beleid vormgeven, niet naar zoekwerk.",
    f_head="Vertel ons welk dossier je wilt opvolgen",                                # F01
    f_intro="Met je antwoord bouwen we een monitor op jouw maat en plannen we je gratis onboardingsessie in.",  # F02 (changed by S&S, deviates from spec)
    step_of="Stap {n} van {t}",
    l_dossier="Welk Belgisch dossier wil je opvolgen?",                               # F12
    ph_dossier="bv. energiebeleid",
    sugs_label="Vaak gevraagd:",
    sugs=["Energiebeleid", "Stikstof", "Mobiliteit", "AI Act", "CBAM"],
    l_context="Wat is belangrijk voor je organisatie?", optional="optioneel",
    ph_context="Bijvoorbeeld: energiebeleid voor Belgische bedrijven — federale en Vlaamse beleidsvoorstellen, parlementaire vragen en commissiebesprekingen.",  # F13
    help_context="Vertel wat relevant is voor je organisatie. Vermeld eventueel instellingen of onderwerpen die je wilt uitsluiten. Een zoekopdracht formuleren hoeft niet.",  # F14 (changed by S&S, dossier moved to its own step)
    b_continue="Verder", b_back="Terug",
    l_level="Welke monitoring heb je nodig?",                                         # F07
    sr_pick="Kies er één.",
    lvl={"EU": "Europese Unie", "NL": "Nederland", "BE": "België"},                   # F08-F10
    lvl_order=["BE", "EU", "NL"],
    echo_default="Laatste stap. We contacteren je via je werkmailadres om de onboardingsessie in te plannen.",
    echo_with="Laatste stap, daarna bereiden we <b></b> voor je voor.",
    l_name="Naam", ph_name="Je naam",
    l_email="Werkmailadres", ph_email="jij@bedrijf.be",                               # F05
    consent='Ik geef Polpo toestemming om mijn antwoorden te gebruiken om mijn proefaccount aan te maken en mij te contacteren, volgens het <a href="https://polpo.com/privacy-policy/">privacybeleid</a>.',  # (changed by S&S, deviates from spec)
    submit="Aan de slag",                                                             # F15 (changed by S&S, deviates from spec)
    sending="Bezig met verzenden…",
    e_dossier="Vermeld welk dossier je wilt opvolgen.",                               # E01
    e_level="Kies het niveau waarop je dit dossier opvolgt.",
    e_name="We hebben een naam nodig voor je account.",
    e_email="Vul een geldig e-mailadres in.",                                          # E02
    e_consent="We hebben je toestemming nodig om je account voor te bereiden en je te contacteren.",
    e_form="Je aanvraag is niet verzonden. Probeer het opnieuw.",                      # E03
    done_t="Je aanvraag is ontvangen",                                                 # T01
    done_b="We bereiden je proefaccount voor rond het dossier dat je doorgaf en nemen contact op om je onboardingsessie van 30 minuten in te plannen. Tijdens de sessie nemen we de inrichting door en geven we je toegang. Daarna start je monitoring.",  # T02 (changed by S&S, deviates from spec)
    perk="Gratis 1-op-1 onboarding inbegrepen",
    reassure="Je gegevens blijven privé.",
    faq_head="Veelgestelde vragen",
    faq=[("Wat krijg ik?", "Een Polpo-proefaccount met opgeslagen zoekopdrachten en e-mailmeldingen rond jouw dossier. Tijdens de onboardingsessie van 30 minuten nemen we de inrichting door en geven we je toegang."),
         ("Wat gebeurt er nadat ik het formulier invul?", "We gebruiken je antwoorden om je account voor te bereiden en de onboardingsessie met je in te plannen. Met het formulier vraag je een proefaccount aan; je monitoring start na de onboardingsessie en overdracht."),
         ("Waarom hoort er een onboardingsessie bij?", "De sessie vindt plaats in jouw voorbereide account. We controleren je dossier en meldingen, tonen hoe je de monitor gebruikt en aanpast, en geven je toegang om zelf verder te werken."),
         ("Wanneer ontvang ik updates?", "Je monitoring start meteen na de overdracht. Je ontvangt e-mailmeldingen zodra passende informatie beschikbaar is, volgens je instellingen. De eerste nieuwe melding hangt dus af van relevante publicaties en de gekozen frequentie."),
         ("Kan ik mijn dossier of meldingen aanpassen?", "Ja. Je kunt je opgeslagen zoekopdrachten en meldingen zelf aanpassen. Tijdens de onboardingsessie tonen we hoe dat werkt."),
         ("Welke Belgische bronnen zijn inbegrepen?", "Bij de voorbereiding stemmen we af welke beschikbare Belgische bronnen relevant zijn voor jouw dossier. Je ziet de geselecteerde bronnen in je proefaccount."),
         ("Wat gebeurt er met mijn gegevens?", "Je naam, werkmailadres en dossier gaan naar Polpo, zodat we je account kunnen voorbereiden en de onboardingsessie kunnen inplannen. We verkopen ze niet en geven ze niet door. Elke e-mail bevat een uitschrijflink en we verwijderen je gegevens wanneer je dat vraagt.")],
    z_head="Laat je monitor voor je instellen",                                       # Z01 (changed by S&S, deviates from spec)
    z_body="Deel je Belgische dossier. Wij bereiden de inrichting voor en tonen je tijdens een onboardingsessie van 30 minuten hoe je ermee werkt.",  # Z02 (changed by S&S, deviates from spec)
    sticky="Zoekopdrachten en meldingen voorbereid op jouw dossier.",
    foot_tag="Politieke monitoring met AI", polpo_url="https://polpo.com/be-nl/",
)
