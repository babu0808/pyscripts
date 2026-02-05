from gurux_dlms.GXDLMSClient import GXDLMSClient
from gurux_dlms.objects.enums import ObjectType
from gurux_dlms.enums import Authentication, InterfaceType
from gurux_dlms.manufacturersettings import GXManufacturer
from gurux_dlms.GXDLMSException import GXDLMSException
from gurux_dlms.secure.GXDLMSSecureClient import GXDLMSSecureClient
from gurux_dlms.GXByteBuffer import GXByteBuffer

def create_request_frame(client):
    # Create AARQ request frame for Association
    try:
        frame_data = GXByteBuffer()
        client.getApplicationAssociationRequest(frame_data)
        return frame_data
    except GXDLMSException as ex:
        print("Error in creating request frame: ", ex)
        return None

def read_meter_data(client, logical_name, attribute_index=2):
    # Create read request for specific logical name (LN) and attribute index.
    try:
        frame_data = GXByteBuffer()
        client.read(logical_name, attribute_index, frame_data)
        return frame_data
    except GXDLMSException as ex:
        print("Error reading meter data: ", ex)
        return None

def main():
    # Setup the DLMS client with PC association and WRAPPER interface
    client = GXDLMSClient(
        useLogicalNameReferencing=True,  # Using Logical Name referencing
        clientAddress=16,                # Client address for PC
        serverAddress=1,                 # Server address for the smart meter
        authentication=Authentication.NONE,  # No authentication
        password=None                    # No password for NONE authentication
    )

    # Create request frame for association (AARQ)
    request_frame = create_request_frame(client)
    if request_frame:
        print("Request Frame Created: ", request_frame.toString())

    # Example: Read meter data (e.g., Current meter readings or status)
    # Logical Name (LN) of object to read (Replace with your specific LN)
    logical_name = "1.0.1.8.0.255"  # Example: Active energy total
    data_frame = read_meter_data(client, logical_name, attribute_index=2)
    
    if data_frame:
        print("Data Read Frame Created: ", data_frame.toString())
    else:
        print("Failed to create read request frame.")

if __name__ == "__main__":
    main()
