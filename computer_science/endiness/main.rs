fn to_byte_array_from_u32_le(x: u32) -> [u8; 4] {
    x.to_le_bytes()
}

fn to_u32_from_byte_array_le(bytes: &[u8]) -> u32 {
    u32::from_le_bytes(bytes.try_into().expect("array with incorrect length"))
}

fn to_u32_from_byte_array_be(bytes: &[u8]) -> u32 {
    u32::from_be_bytes(bytes.try_into().expect("array with incorrect length"))
}

fn main() {
    let number: u32 = 0x10203040;

    let barray_le = to_byte_array_from_u32_le(number);
    println!("number: {:x}, byte array as LE: {:?}", number, barray_le);
    println!("LE interpretation: 0x{:x}, int value: {}", to_u32_from_byte_array_le(&barray_le), to_u32_from_byte_array_le(&barray_le));
    println!("BE interpretation: 0x{:x}, int value: {}", to_u32_from_byte_array_be(&barray_le), to_u32_from_byte_array_be(&barray_le));
}