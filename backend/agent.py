def support_agent(query):

    query = query.lower()

    if "refund" in query:
        return "Our refund process takes 5-7 business days."

    elif "order" in query:
        return "Please provide your order ID."

    elif "delivery" in query:
        return "Delivery usually takes 3-5 business days."

    elif "cancel" in query:
        return "You can cancel your order before shipment."

    else:
        return "Thank you for contacting customer support."