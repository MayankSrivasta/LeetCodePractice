package practice;



import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.InvalidAlgorithmParameterException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.Base64;
import java.util.ResourceBundle;
import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.SecretKey;
import javax.crypto.spec.GCMParameterSpec;
import javax.crypto.spec.SecretKeySpec;

public class EncryptionUtil {

	private static final String ENCRYPTION_ALGO = "AES/GCM/NoPadding";
	private static final int GCM_TAG_LENGTH = 16;
	private static final String SECRET_KEY_ALGO = "AES";

	static ResourceBundle res = ResourceBundle.getBundle("com.max.report.resources.ApplicationResources");
	static byte[] key = "pE5nm9GhrRFNRjCanEitQtMV4lyHhNrgD/6GvlZloHE=".getBytes();
	private static final Charset UTF_8 = StandardCharsets.UTF_8;
	
	
	public static String encrypt() throws NoSuchPaddingException, NoSuchAlgorithmException,
			InvalidAlgorithmParameterException, InvalidKeyException, BadPaddingException, IllegalBlockSizeException {
		byte[] plainBytes = null;

		File file = new File(res.getString("com.max.report.FILE_PATH"));
		FileInputStream inputStream;
		try {
			inputStream = new FileInputStream(file);
			plainBytes = new byte[(int) file.length()];
			inputStream.read(plainBytes);

			SecureRandom secureRandom = new SecureRandom();
			byte[] iv = new byte[12];
			secureRandom.nextBytes(iv);

			// added this
			byte[] decodedKey = Base64.getDecoder().decode(key);

			SecretKey secretKey = new SecretKeySpec(decodedKey, SECRET_KEY_ALGO);
			final Cipher cipher = Cipher.getInstance(ENCRYPTION_ALGO);
			GCMParameterSpec parameterSpec = new GCMParameterSpec(GCM_TAG_LENGTH * 8, iv); // 128 bit auth tag length
			cipher.init(Cipher.ENCRYPT_MODE, secretKey, parameterSpec);
			byte[] cipherText = cipher.doFinal(plainBytes);
			ByteBuffer byteBuffer = ByteBuffer.allocate(iv.length + cipherText.length);
			byteBuffer.put(iv);
			byteBuffer.put(cipherText);
			byte[] cipherMessage = byteBuffer.array();
			inputStream.close();
			return Base64.getEncoder().encodeToString(cipherMessage);

		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (Exception e) {
			e.printStackTrace();
		}
		return null;
	}

	public static String decrypt() throws NoSuchPaddingException, NoSuchAlgorithmException,
			InvalidAlgorithmParameterException, InvalidKeyException, BadPaddingException, IllegalBlockSizeException {
		// Security.setProperty("crypto.policy", "unlimited");
		byte[] plainBytes = null;
		File file = new File(res.getString("com.max.report.ENCRYPTED_FILE"));
		FileInputStream inputStream;
		byte[] cipherText = null;
		Cipher cipher = null;
		byte[] returnString = null;
		String decryptData ="";
		try {
			
			String data = readFileAsString();

			byte[] payload = Base64.getDecoder().decode(data);
			
			ByteBuffer byteBuffer = ByteBuffer.wrap(payload);
			
//			
//			inputStream = new FileInputStream(file);
//
//			plainBytes = new byte[(int) file.length()];
//
//			inputStream.read(plainBytes);

			

			byte[] iv = new byte[12];
			byteBuffer.get(iv);

			cipherText = new byte[byteBuffer.remaining()];

			byteBuffer.get(cipherText);

			cipher = Cipher.getInstance(ENCRYPTION_ALGO);

			// added this
			byte[] decodedKey = Base64.getDecoder().decode(key);

			cipher.init(Cipher.DECRYPT_MODE, new SecretKeySpec(decodedKey, SECRET_KEY_ALGO),
					new GCMParameterSpec(GCM_TAG_LENGTH * 8, iv));

//		} catch (FileNotFoundException e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//	
			 returnString = cipher.doFinal(cipherText);
			 decryptData = new String(returnString);
		}
		catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		return decryptData;
	}

	public static String readFileAsString() {
		String data = "";
		try {
			data = new String(Files.readAllBytes(Paths.get(res.getString("com.max.report.ENCRYPTED_FILE"))));
		} catch (IOException e) {
			e.printStackTrace();
		}

		return data;
	}
}
