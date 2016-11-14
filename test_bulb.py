import unittest
from bulb_classes import LightBulb, LightBulbFactory

class LightBulbTest(unittest.TestCase):
    # use the setUp() method to create an instance of LightBulbFactory & a new LightBulb
    def setUp(self):
        self.bulb_factory = LightBulbFactory()
        self.bulb = self.bulb_factory.create_bulb("GE")

    # test if "bulb" is indeed an instance of LightBulb
    def testNewBulbIsLightBulb(self):
        return self.assertIsInstance(self.bulb, LightBulb)

    # test if "bulb" has a brand property
    def testBulbHasBrand(self):
        return self.assertEqual("GE", self.bulb.brand)

    # test that "bulb" is off by default
    def testBulbDefaultOff(self):
        return self.assertEqual(False, self.bulb.on_or_off())

    # test that "bulb" can be switched on from the off status
    def testTurnOnBulb(self):
        self.bulb.switch_on()
        return self.assertEqual(True, self.bulb.on_or_off())

if __name__ == "__main__":
    unittest.main()
