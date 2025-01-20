from tinydb import TinyDB, Query
import logging

class API:
    """ The base class for all the API handlers"""
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.authenticated = False
        self.user_name = None
        self.user_email = None
        self.is_active = False
        self.user_id = None

    def login(self, username, password):
        """Authenticate with the API using the provided username and password."""
        try:
            User = Query()
            user_data = self.db.table("users").get((User.username == username) & (User.password == password))
            if user_data:
                self.authenticated = True
                self.user_id = user_data.doc_id
                self.user_name = user_data['username']
                self.user_email = user_data['email']
                self.is_active = user_data['active']
                return user_data
            else:
                logging.error("Failed to login: Invalid credentials")
                return None
        except Exception as e:
            logging.error(f"Failed to login: {e}")
            return None
    def Refresh_token(self):
        """Refresh the token."""
        p
    def login_as_admin(self, username, password):
        """Authenticate with the API using the provided username and password."""
        try:
            User = Query()
            user_data = self.db.table("superusers").get((User.username == username) & (User.password == password))
            if user_data:
                self.authenticated = True
                self.user_id = user_data.doc_id
                return user_data
            else:
                logging.error("Failed to login as admin: Invalid credentials")
                return None
        except Exception as e:
            logging.error(f"Failed to login as admin: {e}")
            return None

    def logout(self):
        """Log out the current user."""
        try:
            self.authenticated = False
            self.user_name = None
            self.user_email = None
            self.is_active = False
            self.user_id = None
            return True
        except Exception as e:
            logging.error(f"Failed to logout: {e}")
            return False

    def create_AH_cycle(self, data):
        """Create a cycle."""
        try:
            return self.db.table("adaptive_hedge_cycles").insert(data)
        except Exception as e:
            logging.error(f"Failed to create AH cycle: {e}")
            return None

    def delete_AH_cycle(self, cycle_id):
        """Delete a cycle."""
        try:
            return self.db.table("adaptive_hedge_cycles").remove(doc_ids=[cycle_id])
        except Exception as e:
            logging.error(f"Failed to delete AH cycle: {e}")
            return None

    def get_AH_cycle_by_id(self, cycle_id):
        """Get a cycle by its ID."""
        try:
            return self.db.table("adaptive_hedge_cycles").get(doc_id=cycle_id)
        except Exception as e:
            logging.error(f"Failed to get AH cycle by ID: {e}")
            return None

    def get_AH_active_cycles(self):
        """Get all active cycles."""
        try:
            Cycle = Query()
            return self.db.table("adaptive_hedge_cycles").search(Cycle.is_closed == False)
        except Exception as e:
            logging.error(f"Failed to get AH active cycles: {e}")
            return None

    def update_AH_cycle_by_id(self, cycle_id, data):
        """Update a cycle by its ID."""
        try:
            return self.db.table("adaptive_hedge_cycles").update(data, doc_ids=[cycle_id])
        except Exception as e:
            logging.error(f"Failed to update AH cycle by ID: {e}")
            return None

    def get_AH_cycle_by_cycle_id(self, cycle_id):
        """Get a cycle by its cycle ID."""
        try:
            Cycle = Query()
            return self.db.table("adaptive_hedge_cycles").search(Cycle.cycle_id == cycle_id)
        except Exception as e:
            logging.error(f"Failed to get AH cycle by cycle ID: {e}")
            return None

    def close_AH_cycle(self, cycle_id):
        """Close a cycle by its ID."""
        try:
            data = {"is_closed": True}
            return self.db.table("adaptive_hedge_cycles").update(data, doc_ids=[cycle_id])
        except Exception as e:
            logging.error(f"Failed to close AH cycle: {e}")
            return None

    def create_CT_cycle(self, data):
        """Create a cycle."""
        try:
            return self.db.table("cycles_trader_cycles").insert(data)
        except Exception as e:
            logging.error(f"Failed to create CT cycle: {e}")
            return None

    def delete_CT_cycle(self, cycle_id):
        """Delete a cycle."""
        try:
            return self.db.table("cycles_trader_cycles").remove(doc_ids=[cycle_id])
        except Exception as e:
            logging.error(f"Failed to delete CT cycle: {e}")
            return None

    def get_CT_cycle_by_id(self, cycle_id):
        """Get a cycle by its ID."""
        try:
            return self.db.table("cycles_trader_cycles").get(doc_id=cycle_id)
        except Exception as e:
            logging.error(f"Failed to get CT cycle by ID: {e}")
            return None

    def get_CT_active_cycles(self):
        """Get all active cycles."""
        try:
            Cycle = Query()
            return self.db.table("cycles_trader_cycles").search(Cycle.is_closed == False)
        except Exception as e:
            logging.error(f"Failed to get CT active cycles: {e}")
            return None

    def update_CT_cycle_by_id(self, cycle_id, data):
        """Update a cycle by its ID."""
        try:
            return self.db.table("cycles_trader_cycles").update(data, doc_ids=[cycle_id])
        except Exception as e:
            logging.error(f"Failed to update CT cycle by ID: {e}")
            return None

    def get_CT_cycle_by_cycle_id(self, cycle_id):
        """Get a cycle by its cycle ID."""
        try:
            Cycle = Query()
            return self.db.table("cycles_trader_cycles").search(Cycle.cycle_id == cycle_id)
        except Exception as e:
            logging.error(f"Failed to get CT cycle by cycle ID: {e}")
            return None

    def close_CT_cycle(self, cycle_id):
        """Close a cycle by its ID."""
        try:
            data = {"is_closed": True}
            return self.db.table("cycles_trader_cycles").update(data, doc_ids=[cycle_id])
        except Exception as e:
            logging.error(f"Failed to close CT cycle: {e}")
            return None

    def create_order(self, data):
        """Create an order."""
        logging.info(f"Creating order with data: {data}")

        # Ensure all required fields are present
        required_fields = ["ticket"]
        for field in required_fields:
            if field not in data:
                logging.error(f"Missing required field: {field}")
                raise ValueError(f"Missing required field: {field}")

        try:
            return self.db.table("Orders").insert(data)
        except Exception as e:
            logging.error(f"Failed to create order: {e}")
            return None

    def delete_order(self, order_id):
        """Delete an order."""
        try:
            return self.db.table("Orders").remove(doc_ids=[order_id])
        except Exception as e:
            logging.error(f"Failed to delete order: {e}")
            return None

    def get_order_by_id(self, order_id):
        """Get an order by its ID."""
        try:
            return self.db.table("Orders").get(doc_id=order_id)
        except Exception as e:
            logging.error(f"Failed to get order by ID: {e}")
            return None

    def update_order_by_id(self, order_id, data):
        """Update an order by its ID."""
        try:
            return self.db.table("Orders").update(data, doc_ids=[order_id])
        except Exception as e:
            logging.error(f"Failed to update order by ID: {e}")
            return None

    def get_order_by_ticket(self, ticket):
        """Get an order by its ticket."""
        try:
            Order = Query()
            return self.db.table("Orders").search(Order.ticket == ticket)
        except Exception as e:
            logging.error(f"Failed to get order by ticket: {e}")
            return None

    def get_open_orders_only(self):
        """Get all open orders."""
        try:
            Order = Query()
            return self.db.table("Orders").search(Order.is_closed == False)
        except Exception as e:
            logging.error(f"Failed to get open orders: {e}")
            return None

    def get_open_pending_orders(self):
        """Get all pending orders."""
        try:
            Order = Query()
            return self.db.table("Orders").search((Order.is_closed == False) & (Order.is_pending == True))
        except Exception as e:
            logging.error(f"Failed to get open pending orders: {e}")
            return None

    def get_mt5_credintials(self):
        """Get all MT5 credentials."""
        try:
            return self.db.table("mt5_auth").all()
        except Exception as e:
            logging.error(f"Failed to get MT5 credentials: {e}")
            return None

    def set_mt5_credintials(self, data):
        """Set MT5 credentials."""
        try:
            return self.db.table("mt5_auth").insert(data)
        except Exception as e:
            logging.error(f"Failed to set MT5 credentials: {e}")
            return None

    def get_pb_credintials(self):
        """Get all PocketBase credentials."""
        try:
            return self.db.table("pb_auth").all()
        except Exception as e:
            logging.error(f"Failed to get PocketBase credentials: {e}")
            return None

    def set_pb_credintials(self, data):
        """Set PocketBase credentials."""
        try:
            return self.db.table("pb_auth").insert(data)
        except Exception as e:
            logging.error(f"Failed to set PocketBase credentials: {e}")
            return None